# 1
# mypkg/__init__.py            (can be empty)
# mypkg/tools.py
def some_function():
    return "hello from tools!"

# elsewhere:
import mypkg.tools
print(mypkg.tools.some_function())    # hello from tools!

# 2
# mypkg/__init__.py
from .tools import some_function

# elsewhere:
import mypkg
print(mypkg.some_function())          # hello from tools!

# 3
# shapes/sizes.py
def double(n):
    return 2 * n

# shapes/main.py
from . import sizes
print(sizes.double(21))               # 42

# Run from the folder above shapes:
#   python -m shapes.main             # works: the package context is "shapes"
#   python shapes/main.py             # ImportError: attempted relative import with no known parent package
