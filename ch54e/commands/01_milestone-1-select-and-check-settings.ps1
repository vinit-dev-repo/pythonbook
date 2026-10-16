py -3.15 -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements-dev.txt
.\.venv\Scripts\python -m pip install --no-deps .
.\.venv\Scripts\python -m pytest -q
.\.venv\Scripts\python -m expense_ledger --config ledger.example.json check
