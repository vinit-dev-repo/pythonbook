.\.venv\Scripts\python -m pip install --no-deps --force-reinstall .
.\.venv\Scripts\python -m pytest -q
.\.venv\Scripts\python -m expense_ledger --db ledger.db --limit 4 init
.\.venv\Scripts\python -m expense_ledger --db ledger.db --limit 4 import batch_ok.json
.\.venv\Scripts\python -m expense_ledger --db ledger.db list
.\.venv\Scripts\python -m expense_ledger --db ledger.db total 2026-08
.\.venv\Scripts\python -m expense_ledger --db ledger.db --limit 4 import batch_conflict.json
.\.venv\Scripts\python -m expense_ledger --db ledger.db list
.\.venv\Scripts\python -m expense_ledger --db ledger.db total 2026-08
