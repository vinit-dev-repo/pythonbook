permissions = READ | WRITE
print(bin(permissions))
print(permissions & READ)
print(bool(permissions & READ))
print(permissions & EXECUTE)
print(bool(permissions & EXECUTE))
