# 1
# checker.py
print(f"__name__ here is: {__name__}")

# When RUN DIRECTLY (python checker.py):   __name__ here is: __main__
# When IMPORTED (import checker):          __name__ here is: checker

# 2
# message.py
def render():
    return "v1"

# client.py
import importlib
from message import render as saved
import message

# ... edit message.py so that render() returns "v2" ...
importlib.invalidate_caches()
importlib.reload(message)
print(saved())                 # v1: the saved function keeps its old body
print(message.render())        # v2: qualification reads the current attribute

# 3
# tool.py
def run():
    print("working")

if __name__ == "__main__":
    run()

# other.py
import tool                    # prints nothing: the guard is false on import
tool.run()                     # working
