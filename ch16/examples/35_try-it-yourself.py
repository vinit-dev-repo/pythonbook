# 6
import math
from decimal import Decimal, getcontext, localcontext

print(math.isclose(0.0, 2e-12, rel_tol=1e-9, abs_tol=1e-12))
print(math.isclose(0.0, 2e-12, rel_tol=1e-9, abs_tol=2e-12))
earlier_precision = getcontext().prec
with localcontext() as ctx:
    ctx.prec = 3
    value = Decimal("2.3456")
    print(value)
    print(value + Decimal("0"))
print(getcontext().prec == earlier_precision)
