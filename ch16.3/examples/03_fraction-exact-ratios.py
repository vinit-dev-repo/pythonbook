from fractions import Fraction

x = Fraction(0.3333333333333333)
print(x)                            # exact ratio of the stored float
print(x.limit_denominator(10))      # closest ratio with denominator <= 10
