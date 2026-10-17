# 1
price = 19.999
print(f"${price:.2f}")   # $20.00

# 2
print(ord("Z"))          # 90
print(chr(9731))         # ☃

# 3
print(len("\U0001F600"))   # 1
print(len("e\u0301"))      # 2: len counts code points, not the shapes you see
