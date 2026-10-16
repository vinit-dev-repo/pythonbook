def replace_cart(cart):
    cart = ["only", "these"]    # this only re-ties the LOCAL name "cart"

groceries = ["eggs", "bread"]
replace_cart(groceries)
print(groceries)                # untouched — groceries still points at the original list
