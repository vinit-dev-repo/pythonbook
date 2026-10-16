from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Never

from .config import ConfigError, Settings, load_settings
from .ledger import (
    Busy,
    Capacity,
    Conflict,
    LedgerError,
    Storage,
    add_many,
    entry_dicts,
    initialize,
    list_entries,
    read_batch,
    total_for_month,
)


class SafeParser(argparse.ArgumentParser):
    def error(self, message: str) -> Never:
        self.exit(2, "E_ARGUMENT\n")


def _minor(value: str) -> int:
    if not value or not value.isascii() or not value.isdecimal():
        raise argparse.ArgumentTypeError("invalid")
    try:
        return int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("invalid") from error


def parser() -> argparse.ArgumentParser:
    result = SafeParser(
        prog="expense-ledger", description="Operate a local expense ledger."
    )
    result.add_argument("--config")
    result.add_argument("--db")
    result.add_argument("--limit")
    result.add_argument("--log-level")
    commands = result.add_subparsers(dest="command", required=True)
    commands.add_parser("check")
    commands.add_parser("init")
    add = commands.add_parser("add")
    add.add_argument("--ref", required=True)
    add.add_argument("--description", required=True)
    add.add_argument("--category", required=True)
    add.add_argument("--minor", required=True, type=_minor)
    add.add_argument("--date", required=True)
    imported = commands.add_parser("import")
    imported.add_argument("file")
    commands.add_parser("list")
    total = commands.add_parser("total")
    total.add_argument("month")
    return result


def _run(args: argparse.Namespace, settings: Settings) -> tuple[str, int]:
    if args.command == "check":
        print("configuration valid")
        return "OK", 0
    if args.command == "init":
        initialize(settings)
        print("initialized")
        return "OK", 0
    if args.command == "add":
        count = add_many(
            settings,
            [
                {
                    "reference": args.ref,
                    "description": args.description,
                    "category": args.category,
                    "amount_minor": args.minor,
                    "spent_on": args.date,
                }
            ],
        )
        print(f"added {count}")
        return "OK", count
    if args.command == "import":
        count = add_many(settings, read_batch(Path(args.file)))
        print(f"imported {count}")
        return "OK", count
    if args.command == "list":
        rows = entry_dicts(list_entries(settings))
        print(json.dumps(rows, separators=(",", ":")))
        return "OK", len(rows)
    total = total_for_month(settings, args.month)
    print(total)
    return "OK", total


def _owned_logger(
    level: str,
) -> tuple[logging.Logger, logging.Handler, Callable[[], None]]:
    logger = logging.getLogger("expense_ledger.operation")
    previous_level = logger.level
    previous_propagate = logger.propagate
    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter("%(levelname)s %(name)s %(message)s"))
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(handler)

    def clean_up() -> None:
        logger.removeHandler(handler)
        handler.close()
        logger.setLevel(previous_level)
        logger.propagate = previous_propagate

    return logger, handler, clean_up


def main(argv: list[str] | None = None) -> int:
    try:
        args = parser().parse_args(argv)
    except SystemExit as error:
        return error.code if type(error.code) is int else 2
    try:
        settings = load_settings(vars(args), os.environ, Path.cwd())
    except ConfigError:
        print("E_CONFIG", file=sys.stderr)
        return 2

    logger, _handler, clean_up = _owned_logger(settings.log_level)
    try:
        try:
            code, count = _run(args, settings)
        except LedgerError as error:
            command = str(args.command)
            logger.error("command=%s code=%s", command, error.code)
            if isinstance(error, (Conflict, Capacity)):
                return 3
            if isinstance(error, Busy):
                return 4
            if isinstance(error, Storage):
                return 1
            return 2
        logger.info("command=%s code=%s count=%s", args.command, code, count)
        return 0
    finally:
        clean_up()
