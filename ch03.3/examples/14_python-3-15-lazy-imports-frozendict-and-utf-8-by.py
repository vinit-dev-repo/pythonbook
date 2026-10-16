import sys

lazy import fractions

print("loaded before use:", "fractions" in sys.modules)
half = fractions.Fraction(1, 2)
print("loaded after use: ", "fractions" in sys.modules)
print(half + half)
