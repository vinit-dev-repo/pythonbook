# Runbook

This is a local, single-user educational ledger. It does not provide encryption,
authentication, currency accounting, backups, cloud deployment or production recovery.

## Set up and check

Run from the project folder with your selected Python 3.15 interpreter:

```powershell
py -3.15 -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements-dev.txt
.\.venv\Scripts\python -m pip install --no-deps .
.\.venv\Scripts\python -m pytest -q
.\.venv\Scripts\python -m expense_ledger --config ledger.example.json check
```

Relative database paths are based on the launch working directory, including a path read
from JSON. For a stable location while changing directories, put an absolute database path
in the command or selected JSON file.

## Operate

Global options precede the command:

```powershell
$ledger = Join-Path (Get-Location) "ledger.db"
.\.venv\Scripts\expense-ledger --db $ledger --limit 4 init
.\.venv\Scripts\expense-ledger --db $ledger --limit 4 import batch_ok.json
.\.venv\Scripts\expense-ledger --db $ledger list
.\.venv\Scripts\expense-ledger --db $ledger total 2026-08
.\.venv\Scripts\expense-ledger --db $ledger --limit 4 add --ref note --description Notebook --category Other --minor 500 --date 2026-08-09
.\.venv\Scripts\expense-ledger --db $ledger list
.\.venv\Scripts\expense-ledger --db $ledger total 2026-08
```

`init` is repeatable and never seeds. `add` prints `added 1`; `import` prints `imported N`.
`list` prints ordered complete JSON records. `total` prints integer minor units.
The first list has Bus, Lunch and Train and the first total is `2370`. After the distinct
Notebook row, the second list has four records and the second total is `2870`.

## Exit meanings and recovery

- 0: success. Read with `list` or `total` when you need to verify state.
- 2: command, configuration or record input is invalid. Correct the input and rerun.
- 3: conflict or capacity. Read the rows and total; the failed group was rolled back.
  Correct the duplicate or reduce the new batch. A lower limit never deletes old rows.
- 4: another writer holds SQLite's write lock. Identify and release that demonstrated
  owner, read the state, then retry deliberately. The program does not retry for you.
- 1: another storage failure. Preserve the database, check its location/permissions/schema,
  and diagnose in a controlled test or debugger before retrying.

Do not delete the database as routine recovery. Diagnostics use fixed categories so paths,
descriptions, environment contents and original exception messages do not enter the log.
`timeout=0` removes SQLite lock waiting; it is not a hard deadline for disk or OS work.
Initialization can leave an empty file if setup fails, so no byte-for-byte rollback promise is
made. The contract is about logical rows and totals.
