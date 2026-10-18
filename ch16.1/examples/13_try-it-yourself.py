import math

# 1
print(2 ** 200)          # a huge exact integer, no overflow
print(int("101", 2))     # 5: "101" read as binary

# 2
print(0.1 + 0.2 != 0.3)                # True: they are NOT equal as floats
print(math.isclose(0.1 + 0.2, 0.3))    # True: close enough

# 3
print(math.isclose(0.0, 2e-12, rel_tol=1e-9, abs_tol=1e-12))   # False
print(math.isclose(0.0, 2e-12, rel_tol=1e-9, abs_tol=2e-12))   # True
