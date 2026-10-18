import sys
from io import StringIO

original_input = sys.stdin
try:
    sys.stdin = StringIO("\n")
    print("Blank line:", repr(input()))
    try:
        input()
    except EOFError:
        print("No input remains: EOFError")
finally:
    sys.stdin = original_input
