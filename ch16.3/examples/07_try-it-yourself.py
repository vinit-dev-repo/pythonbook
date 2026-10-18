from fractions import Fraction

# 1
print(Fraction(1, 10) + Fraction(2, 10))   # 3/10
print(0.1 + 0.2)                           # 0.30000000000000004

# 2
numerator, denominator = (0.625).as_integer_ratio()
print(numerator, denominator, Fraction(numerator, denominator))   # 5 8 5/8
print(Fraction("0.2") == Fraction(1, 5))   # True
print(Fraction(0.2) == Fraction(1, 5))     # False

# 3
z = complex(3, -2)
print(z * 1j)           # (2+3j)
print(z.conjugate())    # (3+2j)
print(z + 5)            # (8-2j)
print(sorted([z, complex(1, 1)], key=abs))   # [(1+1j), (3-2j)]
