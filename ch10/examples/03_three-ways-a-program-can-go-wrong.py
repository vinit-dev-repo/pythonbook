price = 100
tax_rate = 0.2
total = price + tax_rate      # bug: should be price + price * tax_rate
print(total)
