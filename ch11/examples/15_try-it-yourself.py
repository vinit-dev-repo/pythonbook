# 1  (math_tools.py)
def square(n):
    return n * n

# 1  (main.py)
import math_tools
print(math_tools.square(5))   # 25

# 2  (add to math_tools.py)
if __name__ == "__main__":
    print("math_tools ready")

# 3
with open("shopping.txt", "w", encoding="utf-8") as f:
    f.write("milk\nbread\neggs\n")

with open("shopping.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
# milk
# bread
# eggs

# 4
from pathlib import Path
report = Path("output") / "report.csv"
print(report.exists())   # False, unless you actually have that file

# 5
# "w" truncates existing contents; "a" keeps them and adds to the end.
