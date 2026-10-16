from decimal import Decimal, localcontext

# 2. Temporarily use more decimal places, then go back to normal
with localcontext() as ctx:
    ctx.prec = 50                     # 50 digits of precision, but ONLY inside this block
    print(Decimal(1) / Decimal(7))

print(Decimal(1) / Decimal(7))        # back to the normal (default) precision
