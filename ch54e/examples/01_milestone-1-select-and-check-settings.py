from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Never

from .config import ConfigError, load_settings


class SafeParser(argparse.ArgumentParser):
    def error(self, message: str) -> Never:
        self.exit(2, "E_ARGUMENT\n")


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
    return result


def main(argv: list[str] | None = None) -> int:
    try:
        args = parser().parse_args(argv)
    except SystemExit as error:
        return error.code if type(error.code) is int else 2
    try:
        load_settings(vars(args), os.environ, Path.cwd())
    except ConfigError:
        print("E_CONFIG", file=sys.stderr)
        return 2
    print("configuration valid")
    return 0
