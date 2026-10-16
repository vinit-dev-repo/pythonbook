a = 0b1100        # 12, written in binary
b = 0b1010        # 10

print(bin(a & b))     # AND  - 1 only where BOTH have 1
print(bin(a | b))     # OR   - 1 where EITHER has 1
print(bin(a ^ b))     # XOR  - 1 where they DIFFER
print(bin(a << 1))    # shift left  - each move doubles
print(bin(a >> 1))    # shift right - each move halves
