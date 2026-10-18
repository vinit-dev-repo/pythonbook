import math
from decimal import Decimal, ROUND_HALF_UP, getcontext, localcontext

# 1
x = -4.5
print(int(x))            # -4: truncates toward zero
print(math.floor(x))     # -5: rounds down the number line
print(math.ceil(x))      # -4: rounds up the number line
print(round(x))          # -4: nearest EVEN whole number (banker's rounding)

# 2
price = Decimal("2.85")
total = price * 4
print(total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))   # 11.40

# 4
earlier_precision = getcontext().prec
with localcontext() as ctx:
    ctx.prec = 3
    value = Decimal("2.3456")
    print(value)                    # 2.3456
    print(value + Decimal("0"))     # 2.35
print(getcontext().prec == earlier_precision)   # True
