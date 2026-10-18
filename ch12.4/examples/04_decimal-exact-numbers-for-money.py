from decimal import Decimal

total = Decimal("19.995")
rounded = total.quantize(Decimal("0.01"))
print(rounded)
