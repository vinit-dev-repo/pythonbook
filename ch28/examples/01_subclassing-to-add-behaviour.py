from collections import namedtuple

class Point(namedtuple("Point", "x y")):
    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

p = Point(3, 4)
print(p.distance_from_origin())
