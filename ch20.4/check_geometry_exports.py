# check_geometry_exports.py
from geometry_demo import *
print("diameter" in globals())
print("triangle" in globals())
from geometry_demo import triangle
print(triangle.perimeter(3, 4, 5))
