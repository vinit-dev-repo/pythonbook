# 1
print(2 ** 200)          # a huge exact integer, no overflow
print(int("101", 2))     # 5 — "101" read as binary

# 2
print(0.1 + 0.2 != 0.3)  # True — they are NOT equal as floats
import math
print(math.isclose(0.1 + 0.2, 0.3))   # True — close enough

# 3
import math
x = -4.5
print(int(x))            # -4 — truncates toward zero
print(math.floor(x))     # -5 — rounds down the number line
print(math.ceil(x))      # -4 — rounds up the number line
print(round(x))          # -4 — nearest EVEN whole number (banker's rounding)

# 4
from decimal import Decimal, ROUND_HALF_UP
price = Decimal("2.85")
total = price * 4
print(total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))   # 11.40

# 5
scores = [True, True, False, True, False]
print(sum(scores))       # 3
