# reload_check.py
import importlib
import shape

old_module = shape
old_class = shape.Circle
c = shape.Circle()

importlib.reload(shape)
new_circle = shape.Circle()

print("same module:", shape is old_module)
print("same class binding:", shape.Circle is old_class)
print("old instance class:", c.__class__ is old_class)
print("old instance passes new check:", isinstance(c, shape.Circle))
print("new instance passes new check:", isinstance(new_circle, shape.Circle))
