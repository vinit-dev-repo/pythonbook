def make(i):
    return lambda: f"button {i}"

handlers = [make(i) for i in range(4)]
print([h() for h in handlers])
