py -3.15 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-dev.txt -e ".[test]"
.venv\Scripts\python.exe -m pytest -q
.venv\Scripts\python.exe -m shop_report.cli
