Point = namedtuple("Point", "x y")
Point3D = namedtuple("Point3D", Point._fields + ("z",))
print(Point3D(1, 2, 3))
