from __future__ import annotations

import json
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import NamedTuple


class ConfigError(ValueError):
    """A settings boundary failure with one safe public code."""


@dataclass(frozen=True)
class Settings:
    db_path: Path
    max_records: int
    log_level: str


class Choice(NamedTuple):
    source: str
    value: object


DEFAULTS: dict[str, object] = {
    "db_path": "ledger.db",
    "max_records": 100,
    "log_level": "INFO",
}
ALLOWED = frozenset(DEFAULTS)


def _read_limited(path: Path, limit: int) -> bytes:
    try:
        with path.open("rb") as stream:
            raw = stream.read(limit + 1)
    except (OSError, ValueError) as error:
        raise ConfigError("E_CONFIG") from error
    if len(raw) > limit:
        raise ConfigError("E_CONFIG")
    return raw


def _config_values(path: Path) -> dict[str, object]:
    raw = _read_limited(path, 4096)
    try:
        value = json.loads(raw.decode("utf-8"))
    except (
        UnicodeDecodeError,
        json.JSONDecodeError,
        ValueError,
        RecursionError,
    ) as error:
        raise ConfigError("E_CONFIG") from error
    if type(value) is not dict or set(value) - ALLOWED:
        raise ConfigError("E_CONFIG")
    return value


def _limit(choice: Choice) -> int:
    value = choice.value
    if choice.source in {"environment", "command_line"}:
        if (
            type(value) is not str
            or not value
            or not value.isascii()
            or not value.isdecimal()
        ):
            raise ConfigError("E_CONFIG")
        try:
            converted = int(value)
        except ValueError as error:
            raise ConfigError("E_CONFIG") from error
    else:
        if type(value) is not int:
            raise ConfigError("E_CONFIG")
        converted = value
    if not 1 <= converted <= 1000:
        raise ConfigError("E_CONFIG")
    return converted


def _validate(choices: Mapping[str, Choice], cwd: Path) -> Settings:
    db_value = choices["db_path"].value
    level_value = choices["log_level"].value
    if (
        type(db_value) is not str
        or not db_value
        or db_value.isspace()
        or not db_value.isprintable()
    ):
        raise ConfigError("E_CONFIG")
    if type(level_value) is not str or level_value not in {"INFO", "WARNING"}:
        raise ConfigError("E_CONFIG")
    selected = Path(db_value)
    db_path = selected if selected.is_absolute() else cwd / selected
    return Settings(db_path, _limit(choices["max_records"]), level_value)


def load_settings(
    overrides: Mapping[str, object], environ: Mapping[str, str], cwd: Path
) -> Settings:
    """Merge explicit inputs without reading process globals."""
    choices = {key: Choice("default", value) for key, value in DEFAULTS.items()}
    config_name = overrides.get("config")
    if config_name is not None:
        if (
            type(config_name) is not str
            or not config_name
            or config_name.isspace()
            or not config_name.isprintable()
        ):
            raise ConfigError("E_CONFIG")
        selected = Path(config_name)
        config_path = selected if selected.is_absolute() else cwd / selected
        choices.update(
            {
                key: Choice("json", value)
                for key, value in _config_values(config_path).items()
            }
        )

    environment = {
        "db_path": environ.get("EXPENSE_DB"),
        "max_records": environ.get("EXPENSE_LIMIT"),
        "log_level": environ.get("EXPENSE_LOG_LEVEL"),
    }
    for key, environment_value in environment.items():
        if environment_value is not None:
            choices[key] = Choice("environment", environment_value)

    command_line = {
        "db_path": overrides.get("db"),
        "max_records": overrides.get("limit"),
        "log_level": overrides.get("log_level"),
    }
    for key, command_value in command_line.items():
        if command_value is not None:
            choices[key] = Choice("command_line", command_value)
    return _validate(choices, cwd)
