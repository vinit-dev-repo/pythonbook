# package_star/unbound/check.py
import sys
from export_demo import *
print("child" in globals())
print("export_demo.child" in sys.modules)
print(child.VALUE if hasattr(child, "VALUE") else child)
