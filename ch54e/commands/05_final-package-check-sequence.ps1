.\.venv\Scripts\python -m ruff format --check src tests
.\.venv\Scripts\python -m ruff check src tests
.\.venv\Scripts\python -m mypy
.\.venv\Scripts\python -m pytest -q
.\.venv\Scripts\python -m build --outdir ..\dist
