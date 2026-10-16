from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


def invoke(
    command: list[str], cwd: Path, environment: dict[str, str]
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        env=environment,
        text=True,
        capture_output=True,
        check=False,
    )


def expect(
    result: subprocess.CompletedProcess[str],
    status: int,
    stdout: str,
    stderr: str,
) -> None:
    assert result.returncode == status
    assert result.stdout == stdout
    assert result.stderr == stderr
    assert "ASSESS-PRIVATE" not in result.stdout + result.stderr


def add_arguments(record: dict[str, Any]) -> list[str]:
    return [
        "add",
        "--ref",
        record["reference"],
        "--description",
        record["description"],
        "--category",
        record["category"],
        "--minor",
        str(record["amount_minor"]),
        "--date",
        record["spent_on"],
    ]


def expected_rows(records: list[dict[str, Any]]) -> str:
    ordered = sorted(records, key=lambda item: (item["spent_on"], item["reference"]))
    return json.dumps(ordered, separators=(",", ":")) + "\n"


def main(arguments: list[str] | None = None) -> int:
    selected = sys.argv[1:] if arguments is None else arguments
    if len(selected) != 1:
        raise SystemExit("usage: assess_ledger.py assessment_batch.json")
    fixture_path = Path(selected[0]).resolve()
    fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
    assert set(fixture) == {"initial", "conflict", "corrected", "fifth"}

    python = Path(sys.executable).resolve()
    console = python.parent / "expense-ledger.exe"
    assert console.is_file()
    base_environment = {
        key: value
        for key, value in os.environ.items()
        if key.upper()
        not in {
            "PYTHONPATH",
            "PYTHONHOME",
            "EXPENSE_DB",
            "EXPENSE_LIMIT",
            "EXPENSE_LOG_LEVEL",
        }
    }
    base_environment["PYTHONUTF8"] = "1"
    base_environment["EXPENSE_LIMIT"] = "3"

    origin = invoke(
        [
            str(python),
            "-c",
            "import expense_ledger; print(expense_ledger.__file__)",
        ],
        fixture_path.parent,
        base_environment,
    )
    assert origin.returncode == 0 and origin.stderr == ""
    origin_path = Path(origin.stdout.strip()).resolve()
    site_packages = (python.parent.parent / "Lib" / "site-packages").resolve()
    assert origin_path.is_relative_to(site_packages)

    with tempfile.TemporaryDirectory(prefix="cap1_assessment_") as temporary:
        root = Path(temporary)
        first_cwd = root / "first"
        later_cwd = root / "later"
        first_cwd.mkdir()
        later_cwd.mkdir()
        database = (root / "absolute-ledger.db").resolve()
        config = first_cwd / "settings.json"
        config.write_text(
            json.dumps(
                {
                    "db_path": str(database),
                    "max_records": 2,
                    "log_level": "INFO",
                }
            ),
            encoding="utf-8",
        )
        malformed = first_cwd / "malformed.json"
        malformed.write_text('{"dummy-secret":"ASSESS-PRIVATE"', encoding="utf-8")
        conflict_path = first_cwd / "conflict.json"
        corrected_path = first_cwd / "corrected.json"
        conflict_path.write_text(json.dumps(fixture["conflict"]), encoding="utf-8")
        corrected_path.write_text(json.dumps(fixture["corrected"]), encoding="utf-8")

        module = [str(python), "-m", "expense_ledger"]
        entry = [str(console)]
        common = ["--config", str(config), "--limit", "4"]
        expect(
            invoke(
                module + ["--config", str(malformed), "check"],
                first_cwd,
                base_environment,
            ),
            2,
            "",
            "E_CONFIG\n",
        )
        assert not database.exists()
        expect(
            invoke(module + common + ["init"], first_cwd, base_environment),
            0,
            "initialized\n",
            "INFO expense_ledger.operation command=init code=OK count=0\n",
        )
        expect(
            invoke(entry + common + ["init"], first_cwd, base_environment),
            0,
            "initialized\n",
            "INFO expense_ledger.operation command=init code=OK count=0\n",
        )
        for index, record in enumerate(fixture["initial"]):
            launcher = module if index % 2 == 0 else entry
            expect(
                invoke(
                    launcher + common + add_arguments(record),
                    first_cwd,
                    base_environment,
                ),
                0,
                "added 1\n",
                "INFO expense_ledger.operation command=add code=OK count=1\n",
            )

        rows = expected_rows(fixture["initial"])
        expect(
            invoke(entry + common + ["list"], later_cwd, base_environment),
            0,
            rows,
            "INFO expense_ledger.operation command=list code=OK count=3\n",
        )
        expect(
            invoke(module + common + ["total", "2026-09"], later_cwd, base_environment),
            0,
            "2699\n",
            "INFO expense_ledger.operation command=total code=OK count=2699\n",
        )
        expect(
            invoke(
                entry + common + ["import", str(conflict_path)],
                later_cwd,
                base_environment,
            ),
            3,
            "",
            "ERROR expense_ledger.operation command=import code=E_CONFLICT\n",
        )
        expect(
            invoke(module + common + ["list"], later_cwd, base_environment),
            0,
            rows,
            "INFO expense_ledger.operation command=list code=OK count=3\n",
        )
        expect(
            invoke(
                entry + common + ["total", "2026-09"],
                later_cwd,
                base_environment,
            ),
            0,
            "2699\n",
            "INFO expense_ledger.operation command=total code=OK count=2699\n",
        )
        expect(
            invoke(
                module + common + ["import", str(corrected_path)],
                later_cwd,
                base_environment,
            ),
            0,
            "imported 1\n",
            "INFO expense_ledger.operation command=import code=OK count=1\n",
        )
        four = fixture["initial"] + fixture["corrected"]
        expect(
            invoke(entry + common + ["list"], later_cwd, base_environment),
            0,
            expected_rows(four),
            "INFO expense_ledger.operation command=list code=OK count=4\n",
        )
        expect(
            invoke(module + common + ["total", "2026-09"], later_cwd, base_environment),
            0,
            "2949\n",
            "INFO expense_ledger.operation command=total code=OK count=2949\n",
        )
        expect(
            invoke(
                entry + common + add_arguments(fixture["fifth"]),
                later_cwd,
                base_environment,
            ),
            3,
            "",
            "ERROR expense_ledger.operation command=add code=E_CAPACITY\n",
        )
        expect(
            invoke(module + common + ["list"], later_cwd, base_environment),
            0,
            expected_rows(four),
            "INFO expense_ledger.operation command=list code=OK count=4\n",
        )
        expect(
            invoke(entry + common + ["total", "2026-09"], later_cwd, base_environment),
            0,
            "2949\n",
            "INFO expense_ledger.operation command=total code=OK count=2949\n",
        )
    print("installed assessment: exact persistence and failure contracts observed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
