from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from expense_ledger import ledger
from expense_ledger.config import Settings
from expense_ledger.ledger import (
    Busy,
    Capacity,
    Conflict,
    Entry,
    LedgerError,
    Storage,
    add_many,
    initialize,
    list_entries,
    read_batch,
    total_for_month,
    validate_entry,
    validate_month,
)


def settings(path: Path, limit: int = 4) -> Settings:
    return Settings(path, limit, "WARNING")


def row(reference: str, amount: int = 350, day: int = 3) -> dict[str, object]:
    return {
        "reference": reference,
        "description": reference.title(),
        "category": "Transport",
        "amount_minor": amount,
        "spent_on": f"2026-08-{day:02d}",
    }


def initial_rows() -> list[dict[str, object]]:
    return [
        row("bus", 350, 3),
        {**row("lunch", 820, 4), "category": "Food"},
        row("train", 1200, 8),
    ]


def assert_conflict_state(add=add_many) -> None:
    selected = settings(Path("ledger.db"), 4)
    statements: list[str] = []
    original = ledger.sqlite3.connect

    def traced_connect(*args, **kwargs):
        connection = original(*args, **kwargs)
        connection.set_trace_callback(statements.append)
        return connection

    ledger.sqlite3.connect = traced_connect
    try:
        with pytest.raises(Conflict):
            add(selected, [row("new-first", 500, 9), row("bus", 351, 10)])
    finally:
        ledger.sqlite3.connect = original
    inserts = [text for text in statements if text.startswith("INSERT INTO entries")]
    assert len(inserts) == 2
    assert [entry.reference for entry in list_entries(selected)] == [
        "bus",
        "lunch",
        "train",
    ]
    assert total_for_month(selected, "2026-08") == 2370


def test_persistence_order_totals_and_repeat_init(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    selected = settings(tmp_path / "ledger.db")
    initialize(selected)
    initialize(selected)
    assert add_many(selected, initial_rows()) == 3
    expected = [
        Entry("bus", "Bus", "Transport", 350, "2026-08-03"),
        Entry("lunch", "Lunch", "Food", 820, "2026-08-04"),
        Entry("train", "Train", "Transport", 1200, "2026-08-08"),
    ]
    assert list_entries(selected) == expected
    assert total_for_month(selected, "2026-08") == 2370
    assert total_for_month(selected, "2026-09") == 0
    initialize(selected)
    assert list_entries(selected) == expected
    assert total_for_month(selected, "2026-08") == 2370


def test_conflict_rolls_back_after_first_insert(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    selected = settings(tmp_path / "ledger.db")
    initialize(selected)
    add_many(selected, initial_rows())
    assert_conflict_state()


def test_capacity_rolls_back_wholly_valid_batch(tmp_path: Path):
    selected = settings(tmp_path / "ledger.db", 4)
    initialize(selected)
    add_many(selected, initial_rows())
    before = list_entries(selected)
    with pytest.raises(Capacity):
        add_many(selected, [row("one", 1, 9), row("two", 2, 10)])
    assert list_entries(selected) == before
    assert total_for_month(selected, "2026-08") == 2370


def test_real_busy_release_and_deliberate_retry(tmp_path: Path):
    selected = settings(tmp_path / "ledger.db")
    initialize(selected)
    owner = sqlite3.connect(selected.db_path, autocommit=True, timeout=0)
    owner.execute("BEGIN IMMEDIATE")
    try:
        with pytest.raises(Busy):
            add_many(selected, [row("rail", 450, 12)])
        assert list_entries(selected) == []
    finally:
        owner.execute("ROLLBACK")
        owner.close()
    assert add_many(selected, [row("rail", 450, 12)]) == 1
    assert list_entries(selected) == [
        Entry("rail", "Rail", "Transport", 450, "2026-08-12")
    ]
    assert total_for_month(selected, "2026-08") == 450


def test_missing_and_incompatible_databases(tmp_path: Path):
    selected = settings(tmp_path / "missing.db")
    with pytest.raises(Storage):
        list_entries(selected)
    assert not selected.db_path.exists()

    wrong = settings(tmp_path / "wrong.db")
    connection = sqlite3.connect(wrong.db_path)
    connection.execute(
        "CREATE TABLE entries (reference TEXT PRIMARY KEY NOT NULL, "
        "description TEXT NOT NULL, category TEXT NOT NULL, "
        "amount_minor INTEGER NOT NULL, spent_on TEXT NOT NULL)"
    )
    connection.execute(
        "INSERT INTO entries VALUES ('kept', 'Kept', 'Other', 1, '2026-08-01')"
    )
    connection.commit()
    connection.close()
    with pytest.raises(Storage):
        initialize(wrong)
    check = sqlite3.connect(wrong.db_path)
    assert check.execute("SELECT reference FROM entries").fetchall() == [("kept",)]
    check.close()


@pytest.mark.parametrize(
    "change",
    [
        {"reference": "é"},
        {"description": "   "},
        {"category": []},
        {"amount_minor": True},
        {"amount_minor": 1.0},
        {"amount_minor": type("FancyInt", (int,), {})(1)},
        {"amount_minor": 0},
        {"amount_minor": 1_000_001},
        {"spent_on": "2026-W32-1"},
    ],
)
def test_record_domain_is_exact(change: dict[str, object]):
    candidate = row("ok")
    candidate.update(change)
    with pytest.raises(LedgerError):
        validate_entry(candidate)


@pytest.mark.parametrize(
    "reference,description,amount",
    [("r", "x", 1), ("r" * 32, "x" * 80, 1_000_000)],
)
def test_record_inclusive_boundaries(reference: str, description: str, amount: int):
    candidate = row("ok")
    candidate.update(reference=reference, description=description, amount_minor=amount)
    assert validate_entry(candidate).amount_minor == amount


@pytest.mark.parametrize("change", [{"reference": "r" * 33}, {"description": "x" * 81}])
def test_record_length_overflow(change: dict[str, object]):
    candidate = row("ok")
    candidate.update(change)
    with pytest.raises(LedgerError):
        validate_entry(candidate)


def test_forged_entry_and_bad_batch_fail_before_connection(tmp_path: Path, monkeypatch):
    selected = settings(tmp_path / "ledger.db")
    forged = Entry("ok", "Okay", "Other", 1, "2026-08-01")
    object.__setattr__(forged, "amount_minor", True)

    def forbidden(*args, **kwargs):
        raise AssertionError("validation opened the database")

    monkeypatch.setattr(ledger.sqlite3, "connect", forbidden)
    with pytest.raises(LedgerError):
        add_many(selected, [forged])
    with pytest.raises(LedgerError):
        add_many(selected, [])


@pytest.mark.parametrize("month", ["1-01", "2026-00", "2026-13", []])
def test_month_is_canonical(month: object):
    with pytest.raises(LedgerError):
        validate_month(month)


def test_batch_byte_shape_and_domain_boundaries(tmp_path: Path):
    path = tmp_path / "batch.json"
    path.write_bytes(b" " * 65_537)
    with pytest.raises(LedgerError):
        read_batch(path)
    for payload in [
        b"\xff",
        b"{}",
        b"[]",
        b"[" * 1100 + b"]" * 1100,
        b'[{"amount_minor":' + b"9" * 5000 + b"}]",
        b"[" + b"{} ," * 100 + b"{}]",
    ]:
        path.write_bytes(payload)
        with pytest.raises(LedgerError):
            read_batch(path)
    with pytest.raises(LedgerError):
        read_batch(Path("bad\x00name.json"))


class ConnectionProxy:
    def __init__(self, inner: sqlite3.Connection, fail_on: str):
        self.inner = inner
        self.fail_on = fail_on
        self.closed = False

    @property
    def in_transaction(self):
        return self.inner.in_transaction

    def execute(self, sql, parameters=()):
        if sql.startswith(self.fail_on):
            raise sqlite3.OperationalError("private path must not escape")
        return self.inner.execute(sql, parameters)

    def close(self):
        self.closed = True
        self.inner.close()


@pytest.mark.parametrize(
    "fail_on,operation",
    [
        ("SELECT sql FROM sqlite_schema", "schema"),
        ("SELECT reference", "read"),
        ("INSERT INTO entries", "write"),
        ("COMMIT", "commit"),
    ],
)
def test_expected_sql_failures_map_and_close(
    tmp_path: Path, monkeypatch, fail_on: str, operation: str
):
    selected = settings(tmp_path / "ledger.db")
    initialize(selected)
    original = ledger.sqlite3.connect
    proxies: list[ConnectionProxy] = []

    def failing_connect(*args, **kwargs):
        proxy = ConnectionProxy(original(*args, **kwargs), fail_on)
        proxies.append(proxy)
        return proxy

    monkeypatch.setattr(ledger.sqlite3, "connect", failing_connect)
    with pytest.raises(Storage):
        if operation == "read":
            list_entries(selected)
        else:
            add_many(selected, [row("new")])
    assert proxies and all(proxy.closed for proxy in proxies)


def test_success_connections_are_closed(tmp_path: Path, monkeypatch):
    selected = settings(tmp_path / "ledger.db")
    original = ledger.sqlite3.connect
    opened: list[sqlite3.Connection] = []

    def recording_connect(*args, **kwargs):
        connection = original(*args, **kwargs)
        opened.append(connection)
        return connection

    monkeypatch.setattr(ledger.sqlite3, "connect", recording_connect)
    initialize(selected)
    add_many(selected, [row("bus")])
    list_entries(selected)
    total_for_month(selected, "2026-08")
    for connection in opened:
        with pytest.raises(sqlite3.ProgrammingError):
            connection.execute("SELECT 1")
