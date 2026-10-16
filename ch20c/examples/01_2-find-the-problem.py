handlers = []
for i in range(4):
    handlers.append(lambda: f"button {i}")

print([h() for h in handlers])
