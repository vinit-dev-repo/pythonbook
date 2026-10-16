from pathlib import Path

import pytest
from expense_ledger.cli import main


def test_check_has_no_persistent_effect(tmp_path: Path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    assert main(["--db", "ledger.db", "check"]) == 0
    assert capsys.readouterr() == ("configuration valid\n", "")
    assert list(tmp_path.iterdir()) == []


def test_help_does_not_read_settings(tmp_path: Path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("EXPENSE_LIMIT", "dummy-secret")
    assert main(["--help"]) == 0
    streams = capsys.readouterr()
    assert streams.out.startswith("usage: expense-ledger")
    assert streams.err == ""


@pytest.mark.parametrize("arguments", [["--limit", "x", "check"], ["unknown"]])
def test_early_failures_are_one_fixed_safe_line(arguments, capsys):
    assert main(arguments) == 2
    streams = capsys.readouterr()
    expected = "E_CONFIG\n" if "--limit" in arguments else "E_ARGUMENT\n"
    assert streams.out == ""
    assert streams.err == expected
    assert "x" not in streams.err
