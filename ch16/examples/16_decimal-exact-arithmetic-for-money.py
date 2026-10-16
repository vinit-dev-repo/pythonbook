from decimal import Decimal

wrong = Decimal(0.1)          # exact conversion of the already approximate float
right = Decimal("0.1")        # exact decimal one tenth, constructed from text

print(wrong)
print(right)
