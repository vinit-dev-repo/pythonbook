from decimal import Decimal, getcontext, localcontext

starting_precision = getcontext().prec
with localcontext() as ctx:
    ctx.prec = 3
    value = Decimal("1.2345")
    print(value)
    print(value + Decimal("0"))
    print(Decimal(1) / Decimal(3))
print(getcontext().prec == starting_precision)
