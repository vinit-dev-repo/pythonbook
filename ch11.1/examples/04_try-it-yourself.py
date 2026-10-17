# 1  (math_tools.py)
def square(n):
    return n * n

# 1  (main.py)
import math_tools
print(math_tools.square(5))   # 25

# 2  (add to math_tools.py)
if __name__ == "__main__":
    print("math_tools ready")

# 3  (shout.py)
import sys

if len(sys.argv) > 1:
    print(sys.argv[1].upper())     # python shout.py hello  ->  HELLO
else:
    print("NO WORD")
