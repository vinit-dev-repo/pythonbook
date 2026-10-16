circle = CachedCircle(2)
saved_area = circle.area
try:
    circle.radius = -1
except ValueError as error:
    print(error)
print(circle.radius, circle._area == saved_area)

circle.radius = 1e154
print(circle.radius, circle._area is None)
try:
    print(circle.area)
except ValueError as error:
    print(error)
print(circle.radius, circle._area is None)

circle.radius = 1
print(round(circle.area, 2))
