cart_a = [1, 2]
cart_b = cart_a

cart_a = cart_a + [3]     # NOT in-place: a NEW list, only cart_a moves
print(cart_a)
print(cart_b)             # cart_b is untouched
