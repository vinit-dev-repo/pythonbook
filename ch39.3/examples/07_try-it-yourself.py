# 1
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return isinstance(other, Point) and (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))


a = Point(3, 4)
b = Point(3, 4)
d = {a: "corner"}
print(b in d, d[b])

# 2
p = Point(1, 2)
places = {p: "start"}
p.x = 99
print(p in places, len(places))
p.x = 1
print(p in places)

# 3
cells = {(0, 2): 8}
cells[(1, 3)] = 7
print(len(cells))
print(cells.get((2, 2), 0), len(cells))
print((2, 2) in cells)

# 4
status_by_id = {"T7": "pending", "T9": "done", "T12": "pending"}
groups = {}
for key, value in status_by_id.items():
    groups.setdefault(value, []).append(key)
print(groups)
