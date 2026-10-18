basket = []
try:
    basket.append("apple")
    raise ValueError("checkout rejected")
except ValueError:
    print("Failure handled")
print(basket)
