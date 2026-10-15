# dependency_lab/check.py
from model import top
from walk_modules import inspect_modules

visited, trace = inspect_modules(top)
for row in trace:
    print(*row, sep=" | ")
names = [module.__name__ for module in visited]
print("visited:", names)
print("once each:", len(names) == len(set(names)) == 4)
tracked = set(visited)
top.note = "module attributes can change"
print("still tracked:", top in tracked)
