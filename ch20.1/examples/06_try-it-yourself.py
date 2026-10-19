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
# labels.py
"""Small functions for display labels."""

def shout(text):
    return text.upper() + "!"

# check.py
import labels

print(type(labels))            # <class 'module'>
print(labels.__name__)         # labels
print(labels.__doc__)          # Small functions for display labels.

# 4
# item.py
value = 10

# check.py
import sys
import item

del item
print("item" in globals(), "item" in sys.modules)   # False True
