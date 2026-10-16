cart_a = [1, 2]
cart_b = cart_a          # cart_b points at the SAME list

cart_a += [3]             # in-place: mutates the shared list
print(cart_a)
print(cart_b)             # cart_b changed too — same object!
