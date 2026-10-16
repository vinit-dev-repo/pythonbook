from decimal import Decimal, ROUND_HALF_UP

tax_rate = Decimal("0.0725")
subtotal = Decimal("10.00")
tax = subtotal * tax_rate

print(tax)                                                  # more than 2 dp
print(tax.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))  # explicit two-place, half-up policy
