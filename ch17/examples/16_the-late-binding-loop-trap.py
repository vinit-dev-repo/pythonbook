functions = []
for i in range(3):
    functions.append(lambda i=i: i)   # i=i grabs THIS loop's value, right now

for f in functions:
    print(f())
