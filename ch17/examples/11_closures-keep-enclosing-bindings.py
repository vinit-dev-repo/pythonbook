def make_multiplier(factor):
    def multiply(n):
        return n * factor    # "factor" is remembered from make_multiplier
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))
