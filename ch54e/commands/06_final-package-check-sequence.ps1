Set-Location ..
New-Item -ItemType Directory outside-consumer
Set-Location outside-consumer
py -3.15 -m venv .venv
.\.venv\Scripts\python -m pip install --no-index ..\dist\expense_ledger_demo-0.1.0-py3-none-any.whl
Copy-Item ..\expense-ledger\assess_ledger.py, ..\expense-ledger\assessment_batch.json .
.\.venv\Scripts\python -c "import assess_ledger"
.\.venv\Scripts\python assess_ledger.py assessment_batch.json
