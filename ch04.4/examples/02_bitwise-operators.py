READ    = 0b100
WRITE   = 0b010
EXECUTE = 0b001

permissions = READ | WRITE          # switch two on

print("can read?   ", bool(permissions & READ))
print("can execute?", bool(permissions & EXECUTE))

permissions = permissions | EXECUTE    # switch one more on
print("can execute now?", bool(permissions & EXECUTE))

permissions = permissions & ~WRITE     # switch one off
print("can write now?  ", bool(permissions & WRITE))
