def add_item(item, basket=[]):   # the trap
    basket.append(item)
    return basket

print(add_item("apple"))
print(add_item("banana"))   # the "apple" is still there!
