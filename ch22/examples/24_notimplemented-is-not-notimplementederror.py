print(NotImplemented)
print(type(NotImplemented))

try:
    raise NotImplemented
except TypeError as e:
    print(f"TypeError: {e}")
