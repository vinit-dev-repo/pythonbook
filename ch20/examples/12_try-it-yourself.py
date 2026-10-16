# 1
# greetings.py
def hello(name):
    return f"Hello, {name}!"

# main.py
from greetings import hello
print(hello("World"))          # Hello, World!


# 2
# greetings.py (with the added print)
print("greetings.py is running")

def hello(name):
    return f"Hello, {name}!"

# The message prints only once because the SECOND import finds "greetings"
# already stored in sys.modules, and reuses that cached module object
# instead of running the file's code again.


# 3
import sys
print(sys.path[0])
# On most setups this is the folder containing the script you ran —
# it normally comes first in sys.path, unless -P or -I omits it.
# Built-in and frozen modules are handled before the path-based finder.


# 4
# mypkg/__init__.py            (can be empty)
# mypkg/tools.py
def some_function():
    return "hello from tools!"

# elsewhere:
import mypkg.tools
print(mypkg.tools.some_function())    # hello from tools!


# 5
# checker.py
print(f"__name__ here is: {__name__}")

# When RUN DIRECTLY (python checker.py):   __name__ here is: __main__
# When IMPORTED (import checker):          __name__ here is: checker
