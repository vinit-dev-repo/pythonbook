# dependency_lab/model.py
from types import ModuleType

top = ModuleType("top")
left = ModuleType("left")
right = ModuleType("right")
shared = ModuleType("shared")

top.left = left
top.right = right
left.shared = shared
right.left = left
right.shared = shared
shared.back = top
