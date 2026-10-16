uv python pin 3.15
uv lock
uv sync --locked --extra test
uv run --locked --extra test pytest -q
uv run --locked --extra test shop-report
uv build
