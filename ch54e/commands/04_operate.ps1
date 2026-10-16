$ledger = Join-Path (Get-Location) "ledger.db"
.\.venv\Scripts\expense-ledger --db $ledger --limit 4 init
.\.venv\Scripts\expense-ledger --db $ledger --limit 4 import batch_ok.json
.\.venv\Scripts\expense-ledger --db $ledger list
.\.venv\Scripts\expense-ledger --db $ledger total 2026-08
.\.venv\Scripts\expense-ledger --db $ledger --limit 4 add --ref note --description Notebook --category Other --minor 500 --date 2026-08-09
.\.venv\Scripts\expense-ledger --db $ledger list
.\.venv\Scripts\expense-ledger --db $ledger total 2026-08
