class Rect(Shape):
    size = 99                 # a plain int, shadowing the inherited descriptor

r = Rect.__new__(Rect)        # skip __init__ so nothing validates on the way in
r.size = -5                   # no descriptor here, so no check runs
print(r.size)

class Circle(Shape):
    pass

try:
    Circle(-1)
except ValueError as e:
    print("Circle still validates:", e)
