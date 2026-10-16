import sys

try:
    1 / 0
except ZeroDivisionError:
    kind, value, tb = sys.exc_info()
    print("kind :", kind.__name__)
    print("value:", value)
