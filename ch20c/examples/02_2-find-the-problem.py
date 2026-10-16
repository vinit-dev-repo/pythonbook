handlers = [(lambda i=i: f"button {i}") for i in range(4)]
print([h() for h in handlers])
