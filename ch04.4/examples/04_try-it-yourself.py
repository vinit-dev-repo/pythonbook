# 1
print(bin(0b1010 & 0b0110))     # 0b10
print(bin(0b1010 | 0b0110))     # 0b1110

# 2
print(12 << 2)                  # 48
print(12 >> 2)                  # 3

# 3
READ = 0b100
WRITE = 0b010
EXECUTE = 0b001
permissions = READ | EXECUTE
print(bool(permissions & WRITE))    # False
