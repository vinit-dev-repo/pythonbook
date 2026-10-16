python3.15 -m venv .venv
.venv/bin/python -m pip install -e ".[test]" build==1.6.1
.venv/bin/python -m pytest -q
.venv/bin/python -m shop_report.cli
.venv/bin/shop-report
.venv/bin/python -m build
