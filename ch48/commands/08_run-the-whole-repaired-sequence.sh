python -m ruff format --check src tests
python -m ruff check src tests
python -m mypy
python -m pytest -q
python -m build --outdir ../build-final
