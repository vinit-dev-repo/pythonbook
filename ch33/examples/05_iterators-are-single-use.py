numbers = [1, 2, 3]
it = iter(numbers)

for n in it:
    print(n)

print("second loop:")
for n in it:          # same iterator -- already exhausted!
    print(n)
print("(nothing printed above -- it was empty)")
