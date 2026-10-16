class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)             # False — different objects
locations = {p1: "start"}
print(p2 in locations)      # False — p2 looks the same but ISN'T p1
