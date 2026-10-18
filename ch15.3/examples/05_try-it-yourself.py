# 1
def double_it(n):
    n = n * 2
    return n

value = 5
print(double_it(value), value)   # 10 5
value = double_it(value)
print(value)                     # 10

# 2
def add_item(cart):
    cart.append("milk")

def replace_cart(cart):
    cart = ["only", "these"]

groceries = ["eggs", "bread"]
answer = replace_cart(groceries)
print(groceries, answer)         # ['eggs', 'bread'] None
groceries = ["eggs", "bread"]
answer = add_item(groceries)
print(groceries, answer)         # ['eggs', 'bread', 'milk'] None

# 3
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b, a is b, a is c)    # True False True

# 4
result = None
if result is None:
    print("nothing found")
