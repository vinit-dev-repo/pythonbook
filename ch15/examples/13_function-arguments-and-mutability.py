def add_item(cart):
    cart.append("milk")         # mutates the SAME list the caller owns

groceries = ["eggs", "bread"]
add_item(groceries)
print(groceries)
