from __future__ import annotations

from pathlib import Path

import pytest

from expense_ledger.config import ConfigError, Settings, load_settings


def assert_selected_settings(load=load_settings) -> None:
    root = Path.cwd()
    (root / "settings.json").write_text(
        '{"db_path":"file.db","max_records":2,"log_level":"WARNING"}',
        encoding="utf-8",
    )
    settings = load(
        {
            "config": "settings.json",
            "db": "cli.db",
            "limit": "4",
            "log_level": "INFO",
        },
        {
            "EXPENSE_DB": "env.db",
            "EXPENSE_LIMIT": "3",
            "EXPENSE_LOG_LEVEL": "WARNING",
        },
        root,
    )
    assert settings == Settings(root / "cli.db", 4, "INFO")


def test_selected_settings(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.chdir(tmp_path)
    assert_selected_settings()


def test_invalid_lower_priority_fields_can_be_replaced(tmp_path: Path):
    (tmp_path / "settings.json").write_text(
        '{"db_path":[],"max_records":false,"log_level":[]}', encoding="utf-8"
    )
    settings = load_settings(
        {
            "config": "settings.json",
            "db": " kept name.db ",
            "limit": "4",
            "log_level": "INFO",
        },
        {"EXPENSE_LIMIT": "not-digits"},
        tmp_path,
    )
    assert settings == Settings(tmp_path / " kept name.db ", 4, "INFO")


@pytest.mark.parametrize(
    "payload",
    [
        b'{"dummy-secret":"do-not-print"',
        b"[]",
        b'{"dummy-secret":"do-not-print"}',
        b"\xff",
        b"[" * 1100 + b"]" * 1100,
        b'{"max_records":' + b"9" * 5000 + b"}",
    ],
)
def test_bad_selected_file_classes_are_safe(tmp_path: Path, payload: bytes):
    path = tmp_path / "settings.json"
    path.write_bytes(payload)
    with pytest.raises(ConfigError, match="^E_CONFIG$"):
        load_settings({"config": str(path), "db": "later.db"}, {}, tmp_path)


def test_missing_and_oversized_config(tmp_path: Path):
    with pytest.raises(ConfigError, match="^E_CONFIG$"):
        load_settings({"config": "missing.json"}, {}, tmp_path)
    (tmp_path / "large.json").write_bytes(b" " * 4097)
    with pytest.raises(ConfigError, match="^E_CONFIG$"):
        load_settings({"config": "large.json"}, {}, tmp_path)


def test_json_conversion_value_error_is_safe(tmp_path: Path, monkeypatch):
    (tmp_path / "settings.json").write_text("{}", encoding="utf-8")

    def conversion_failure(value):
        raise ValueError("private conversion detail")

    monkeypatch.setattr("expense_ledger.config.json.loads", conversion_failure)
    with pytest.raises(ConfigError, match="^E_CONFIG$"):
        load_settings({"config": "settings.json"}, {}, tmp_path)


@pytest.mark.parametrize(
    "source,value",
    [
        ("environment", "\u0661"),
        ("environment", "1_0"),
        ("command_line", ""),
        ("command_line", "9" * 5000),
    ],
)
def test_selected_limit_must_be_bounded_ascii_decimal(
    tmp_path: Path, source: str, value: str
):
    overrides: dict[str, object] = {"limit": value} if source == "command_line" else {}
    environ = {"EXPENSE_LIMIT": value} if source == "environment" else {}
    with pytest.raises(ConfigError, match="^E_CONFIG$"):
        load_settings(overrides, environ, tmp_path)


@pytest.mark.parametrize("value", [True, 0, 1001, 1.0])
def test_json_limit_is_an_exact_bounded_integer(tmp_path: Path, value: object):
    import json

    (tmp_path / "settings.json").write_text(
        json.dumps({"max_records": value}), encoding="utf-8"
    )
    with pytest.raises(ConfigError, match="^E_CONFIG$"):
        load_settings({"config": "settings.json"}, {}, tmp_path)


@pytest.mark.parametrize("value", ["", "   ", "bad\npath"])
def test_database_path_must_be_nonblank_and_printable(tmp_path: Path, value: str):
    with pytest.raises(ConfigError, match="^E_CONFIG$"):
        load_settings({"db": value}, {}, tmp_path)
