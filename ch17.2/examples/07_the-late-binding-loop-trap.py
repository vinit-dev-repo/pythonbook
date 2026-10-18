functions = []
for i in range(3):
    functions.append(lambda: i)

for f in functions:
    print(f())
