# circle_state.py
import math


class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center = (center_x, center_y)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def translate(self, dx, dy):
        self.center = (self.center[0] + dx, self.center[1] + dy)

    def scale(self, factor):
        self.radius = self.radius * factor


first = Circle(2, -1, 3)
second = Circle(0, 0, 4)
alias = first
old_center = first.center

before_first_query = (first.center, first.radius)
first_area = first.area()
assert (first.center, first.radius) == before_first_query
assert first_area == 9 * math.pi

assert first.translate(-4, 5) is None
assert first.center == (-2, 4)
assert old_center == (2, -1)
assert alias is first
assert (alias.center, alias.radius) == ((-2, 4), 3)
translated_center = first.center

assert first.scale(2) is None
assert (first.center, first.radius) == ((-2, 4), 6)
assert first.center is translated_center
assert (second.center, second.radius) == ((0, 0), 4)

before_second_query = (first.center, first.radius)
second_area = first.area()
assert (first.center, first.radius) == before_second_query
assert second_area == 36 * math.pi

saved_center = first.center
assert first.translate(1, 2) is None
assert (first.center, saved_center, first.radius) == ((-1, 6), (-2, 4), 6)

print(round(first_area, 2))
print(round(second_area, 2))
print(first.center, saved_center, first.radius)
