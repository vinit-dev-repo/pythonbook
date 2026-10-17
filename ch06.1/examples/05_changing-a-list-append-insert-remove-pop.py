shopping = ["apple", "bread", "milk", "eggs"]

shopping.append("tea")
print(shopping)

shopping.insert(0, "coffee")
print(shopping)

shopping.remove("milk")
print(shopping)

last_item = shopping.pop()
print(last_item)
print(shopping)
