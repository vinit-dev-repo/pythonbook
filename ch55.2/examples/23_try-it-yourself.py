# 3
late = []
fixed = []
for n in range(3):
    late.append(lambda: n * 10)
    fixed.append(lambda n=n: n * 10)

print([f() for f in late])
print([f() for f in fixed])
