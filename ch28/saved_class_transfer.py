# saved_class_transfer.py
import importlib
import shape

old_class = shape.Circle
importlib.reload(shape)
saved_circle = old_class()
print(isinstance(saved_circle, old_class))
print(isinstance(saved_circle, shape.Circle))
