import math

print(math.isclose(0.0, 1e-12))
print(math.isclose(0.0, 1e-12, abs_tol=1e-12))
print(math.isclose(0.0, 2e-12, abs_tol=1e-12))
