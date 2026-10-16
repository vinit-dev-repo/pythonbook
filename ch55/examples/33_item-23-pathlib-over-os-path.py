from pathlib import Path

# os.path — string gluing
import os
old_style = os.path.join("data", "2026", "report.csv")

# pathlib — Pythonic
new_style = Path("data") / "2026" / "report.csv"
print(Path(old_style).as_posix())
print(new_style.as_posix())
print(new_style.suffix, new_style.stem)
