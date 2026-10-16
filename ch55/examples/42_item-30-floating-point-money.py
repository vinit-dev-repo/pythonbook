print(0.10 + 0.20)     # not exactly 0.30!

from decimal import Decimal
print(Decimal("0.10") + Decimal("0.20"))
