from decimal import Decimal, ROUND_HALF_UP

price = Decimal("19.99")
quantity = Decimal("3")
total = price * quantity

print(total)
print(total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
