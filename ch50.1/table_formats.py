# table_formats.py
from pathlib import Path
import tempfile
import pandas as pd

original = pd.DataFrame({"parcel": ["007", "012"], "pieces": [2, 5]})
with tempfile.TemporaryDirectory() as folder:
    root = Path(folder)
    json_path = root / "parcels.json"
    excel_path = root / "parcels.xlsx"
    original.to_json(json_path, orient="records")
    original.to_excel(excel_path, sheet_name="Dispatch", index=False,
                      engine="openpyxl")
    from_json = pd.read_json(json_path, orient="records",
                             dtype={"parcel": "str"})
    from_excel = pd.read_excel(excel_path, sheet_name="Dispatch",
                               dtype={"parcel": "str"}, engine="openpyxl")
    for label, table in (("json", from_json), ("excel", from_excel)):
        assert table.to_dict("records") == original.to_dict("records")
        print(label, table["parcel"].tolist(), table["pieces"].sum())
    try:
        pd.read_excel(excel_path, sheet_name="Missing", engine="openpyxl")
    except ValueError:
        print("missing sheet rejected")
