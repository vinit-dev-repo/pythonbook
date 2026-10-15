from __future__ import annotations

import json
import logging
from pathlib import Path

from expense_ledger import cli
from expense_ledger.cli import main


def call(arguments: list[str], capsys) -> tuple[int, str, str]:
    status = main(arguments)
    streams = capsys.readouterr()
    return status, streams.out, streams.err


def test_help_and_check_have_no_database_effect(tmp_path: Path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("EXPENSE_LIMIT", "dummy-secret")
    status, stdout, stderr = call(["--help"], capsys)
    assert status == 0 and stdout.startswith("usage: expense-ledger") and stderr == ""
    monkeypatch.delenv("EXPENSE_LIMIT")
    assert call(["--log-level", "WARNING", "check"], capsys) == (
        0,
        "configuration valid\n",
        "",
    )
    assert list(tmp_path.iterdir()) == []


def test_exact_data_and_logging_streams(tmp_path: Path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    prefix = ["--db", "ledger.db", "--limit", "4"]
    assert call(prefix + ["init"], capsys) == (
        0,
        "initialized\n",
        "INFO expense_ledger.operation command=init code=OK count=0\n",
    )
    assert call(
        prefix
        + [
            "add",
            "--ref",
            "bus",
            "--description",
            "Bus",
            "--category",
            "Transport",
            "--minor",
            "350",
            "--date",
            "2026-08-03",
        ],
        capsys,
    ) == (
        0,
        "added 1\n",
        "INFO expense_ledger.operation command=add code=OK count=1\n",
    )
    expected = json.dumps(
        [
            {
                "reference": "bus",
                "description": "Bus",
                "category": "Transport",
                "amount_minor": 350,
                "spent_on": "2026-08-03",
            }
        ],
        separators=(",", ":"),
    )
    assert call(prefix + ["list"], capsys) == (
        0,
        expected + "\n",
        "INFO expense_ledger.operation command=list code=OK count=1\n",
    )
    assert call(prefix + ["total", "2026-08"], capsys) == (
        0,
        "350\n",
        "INFO expense_ledger.operation command=total code=OK count=350\n",
    )


def test_fixed_failure_lines_and_secret_safety(tmp_path: Path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    secret = "dummy-secret-value"
    (tmp_path / "bad.json").write_text(
        '{"dummy-secret":"dummy-secret-value"', encoding="utf-8"
    )
    malformed = call(["--config", "bad.json", "check"], capsys)
    assert malformed == (
        2,
        "",
        "E_CONFIG\n",
    )
    missing = call(["--db", "missing.db", "list"], capsys)
    assert missing == (
        1,
        "",
        "ERROR expense_ledger.operation command=list code=E_STORAGE\n",
    )
    rejected = call(["add", "--ref", secret], capsys)
    assert rejected == (2, "", "E_ARGUMENT\n")
    visible = malformed[1:] + missing[1:] + rejected[1:]
    assert secret not in "".join(visible)


def test_warning_suppresses_success_but_keeps_error(
    tmp_path: Path, monkeypatch, capsys
):
    monkeypatch.chdir(tmp_path)
    prefix = ["--db", "ledger.db", "--log-level", "WARNING"]
    assert call(prefix + ["init"], capsys) == (0, "initialized\n", "")
    assert call(prefix + ["total", "bad"], capsys) == (
        2,
        "",
        "ERROR expense_ledger.operation command=total code=E_INPUT\n",
    )


def test_import_validates_before_opening_database(tmp_path: Path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "bad-batch.json").write_text('[{"description":"private"}]')
    assert call(["--db", "ledger.db", "import", "bad-batch.json"], capsys) == (
        2,
        "",
        "ERROR expense_ledger.operation command=import code=E_INPUT\n",
    )
    assert not (tmp_path / "ledger.db").exists()
    assert call(["--db", "ledger.db", "import", "bad\x00name.json"], capsys) == (
        2,
        "",
        "ERROR expense_ledger.operation command=import code=E_INPUT\n",
    )
    assert not (tmp_path / "ledger.db").exists()


def test_repeated_main_restores_logger_and_closes_owned_handlers(
    tmp_path: Path, monkeypatch, capsys
):
    monkeypatch.chdir(tmp_path)
    logger = logging.getLogger("expense_ledger.operation")
    before = (list(logger.handlers), logger.level, logger.propagate)
    original = logging.StreamHandler
    made: list[logging.Handler] = []

    class TrackingHandler(original):
        def __init__(self):
            super().__init__()
            self.was_closed = False
            made.append(self)

        def close(self):
            self.was_closed = True
            super().close()

    monkeypatch.setattr(cli.logging, "StreamHandler", TrackingHandler)
    assert main(["--log-level", "WARNING", "check"]) == 0
    assert main(["--log-level", "WARNING", "check"]) == 0
    capsys.readouterr()
    assert (list(logger.handlers), logger.level, logger.propagate) == before
    assert len(made) == 2 and all(handler.was_closed for handler in made)


def test_root_logger_is_unchanged(tmp_path: Path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    root = logging.getLogger()
    before = (list(root.handlers), root.level, root.propagate)
    assert main(["--log-level", "WARNING", "check"]) == 0
    capsys.readouterr()
    assert (list(root.handlers), root.level, root.propagate) == before
