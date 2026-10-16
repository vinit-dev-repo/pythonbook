import pickle
from datetime import date

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

original = {
    "when": date(2024, 1, 1),
    "coords": (3, 4),          # a tuple
    "tags": {"a", "b"},        # a set
    "point": Point(1, 2),      # a custom class instance
}

raw = pickle.dumps(original)
restored = pickle.loads(raw)

print(restored["when"], restored["coords"], sorted(restored["tags"]))
print(restored["point"].x, restored["point"].y)
