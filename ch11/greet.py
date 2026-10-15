# greet.py
import sys

print(sys.argv)

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = "World"

print(f"Hello, {name}!")
