from __future__ import annotations

import json
import re
import sqlite3
from collections.abc import Iterable
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import cast

from .config import Settings


class LedgerError(ValueError):
    code = "E_INPUT"


class Conflict(LedgerError):
    code = "E_CONFLICT"


class Capacity(LedgerError):
    code = "E_CAPACITY"


class Busy(LedgerError):
    code = "E_BUSY"


class Storage(LedgerError):
    code = "E_STORAGE"


@dataclass(frozen=True)
class Entry:
    reference: str
    description: str
    category: str
    amount_minor: int
    spent_on: str


CREATE_SQL = """CREATE TABLE entries (
    reference TEXT PRIMARY KEY NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL CHECK (category IN ('Food', 'Transport', 'Other')),
    amount_minor INTEGER NOT NULL CHECK (
        typeof(amount_minor) = 'integer'
        AND amount_minor BETWEEN 1 AND 1000000
    ),
    spent_on TEXT NOT NULL
)"""


def validate_entry(value: object) -> Entry:
    if isinstance(value, Entry):
        candidate: object = asdict(value)
    else:
        candidate = value
    fields = {
        "reference",
        "description",
        "category",
        "amount_minor",
        "spent_on",
    }
    if type(candidate) is not dict or set(candidate) != fields:
        raise LedgerError()
    values = cast(dict[str, object], candidate)
    reference = values["reference"]
    description = values["description"]
    category = values["category"]
    amount = values["amount_minor"]
    spent_on = values["spent_on"]
    if (
        type(reference) is not str
        or re.fullmatch(r"[A-Za-z0-9_-]{1,32}", reference) is None
    ):
        raise LedgerError()
    if (
        type(description) is not str
        or not 1 <= len(description) <= 80
        or not description.isprintable()
        or not description.strip()
    ):
        raise LedgerError()
    if type(category) is not str or category not in {"Food", "Transport", "Other"}:
        raise LedgerError()
    if type(amount) is not int or not 1 <= amount <= 1_000_000:
        raise LedgerError()
    if type(spent_on) is not str:
        raise LedgerError()
    try:
        parsed = date.fromisoformat(spent_on)
    except ValueError as error:
        raise LedgerError() from error
    if parsed.isoformat() != spent_on:
        raise LedgerError()
    return Entry(reference, description, category, amount, spent_on)


def validate_month(value: object) -> str:
    if type(value) is not str or re.fullmatch(r"[0-9]{4}-[0-9]{2}", value) is None:
        raise LedgerError()
    try:
        canonical = date(int(value[:4]), int(value[5:]), 1).isoformat()[:7]
    except ValueError as error:
        raise LedgerError() from error
    if canonical != value:
        raise LedgerError()
    return value


def read_batch(path: Path) -> list[Entry]:
    try:
        with path.open("rb") as stream:
            raw = stream.read(65_537)
    except (OSError, ValueError) as error:
        raise LedgerError() from error
    if len(raw) > 65_536:
        raise LedgerError()
    try:
        value = json.loads(raw.decode("utf-8"))
    except (
        UnicodeDecodeError,
        json.JSONDecodeError,
        ValueError,
        RecursionError,
    ) as error:
        raise LedgerError() from error
    if type(value) is not list or not 1 <= len(value) <= 100:
        raise LedgerError()
    return [validate_entry(item) for item in value]


def _mapped(error: sqlite3.Error) -> LedgerError:
    code = getattr(error, "sqlite_errorcode", None)
    primary = code & 0xFF if type(code) is int else None
    if primary in {sqlite3.SQLITE_BUSY, sqlite3.SQLITE_LOCKED}:
        return Busy()
    return Storage()


def _schema(connection: sqlite3.Connection) -> None:
    try:
        row = connection.execute(
            "SELECT sql FROM sqlite_schema WHERE type = 'table' AND name = 'entries'"
        ).fetchone()
    except sqlite3.Error as error:
        raise _mapped(error) from error
    if row is None or row[0] != CREATE_SQL:
        raise Storage()


def _close(connection: sqlite3.Connection, failed: bool) -> None:
    try:
        connection.close()
    except sqlite3.Error as error:
        if not failed:
            raise _mapped(error) from error


def initialize(settings: Settings) -> None:
    connection: sqlite3.Connection | None = None
    failed = False
    try:
        try:
            connection = sqlite3.connect(settings.db_path, autocommit=True, timeout=0)
        except sqlite3.Error as error:
            raise _mapped(error) from error
        try:
            row = connection.execute(
                "SELECT sql FROM sqlite_schema "
                "WHERE type = 'table' AND name = 'entries'"
            ).fetchone()
            if row is None:
                connection.execute(CREATE_SQL)
            _schema(connection)
        except sqlite3.Error as error:
            raise _mapped(error) from error
    except LedgerError:
        failed = True
        raise
    finally:
        if connection is not None:
            _close(connection, failed)


def _open_existing(settings: Settings) -> sqlite3.Connection:
    uri = settings.db_path.absolute().as_uri() + "?mode=rw"
    connection: sqlite3.Connection | None = None
    try:
        connection = sqlite3.connect(uri, uri=True, autocommit=True, timeout=0)
        _schema(connection)
        return connection
    except sqlite3.Error as error:
        if connection is not None:
            _close(connection, True)
        raise _mapped(error) from error
    except LedgerError:
        if connection is not None:
            _close(connection, True)
        raise


def _materialize(values: Iterable[object]) -> list[Entry]:
    try:
        candidates = list(values)
    except TypeError as error:
        raise LedgerError() from error
    if not 1 <= len(candidates) <= 100:
        raise LedgerError()
    return [validate_entry(value) for value in candidates]


def add_many(settings: Settings, values: Iterable[object]) -> int:
    entries = _materialize(values)
    connection = _open_existing(settings)
    failed = False
    try:
        try:
            connection.execute("BEGIN IMMEDIATE")
            for entry in entries:
                try:
                    connection.execute(
                        "INSERT INTO entries "
                        "(reference, description, category, amount_minor, spent_on) "
                        "VALUES (?, ?, ?, ?, ?)",
                        (
                            entry.reference,
                            entry.description,
                            entry.category,
                            entry.amount_minor,
                            entry.spent_on,
                        ),
                    )
                except sqlite3.IntegrityError as error:
                    raise Conflict() from error
            count = cast(
                tuple[int],
                connection.execute("SELECT COUNT(*) FROM entries").fetchone(),
            )[0]
            if count > settings.max_records:
                raise Capacity()
            connection.execute("COMMIT")
        except LedgerError:
            raise
        except sqlite3.Error as error:
            raise _mapped(error) from error
    except LedgerError:
        failed = True
        if connection.in_transaction:
            try:
                connection.execute("ROLLBACK")
            except sqlite3.Error:
                pass
        raise
    finally:
        _close(connection, failed)
    return len(entries)


def list_entries(settings: Settings) -> list[Entry]:
    connection = _open_existing(settings)
    failed = False
    try:
        try:
            rows = connection.execute(
                "SELECT reference, description, category, amount_minor, spent_on "
                "FROM entries ORDER BY spent_on, reference"
            ).fetchall()
        except sqlite3.Error as error:
            raise _mapped(error) from error
        return [Entry(*row) for row in rows]
    except LedgerError:
        failed = True
        raise
    finally:
        _close(connection, failed)


def total_for_month(settings: Settings, month: object) -> int:
    selected = validate_month(month)
    connection = _open_existing(settings)
    failed = False
    try:
        try:
            row = connection.execute(
                "SELECT COALESCE(SUM(amount_minor), 0) FROM entries "
                "WHERE substr(spent_on, 1, 7) = ?",
                (selected,),
            ).fetchone()
        except sqlite3.Error as error:
            raise _mapped(error) from error
        return cast(tuple[int], row)[0]
    except LedgerError:
        failed = True
        raise
    finally:
        _close(connection, failed)


def entry_dicts(entries: Iterable[Entry]) -> list[dict[str, object]]:
    return [asdict(entry) for entry in entries]
