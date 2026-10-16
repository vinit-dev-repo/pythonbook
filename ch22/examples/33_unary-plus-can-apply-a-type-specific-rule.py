from decimal import Decimal, localcontext

reading = Decimal("8.7654")
with localcontext() as context:
    context.prec = 3
    rounded = +reading
print(reading, rounded, reading == rounded)
