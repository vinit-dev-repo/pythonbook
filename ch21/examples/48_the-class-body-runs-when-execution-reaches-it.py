created = []
for number in (1, 2):
    class Stamp:
        print("class body", number)
    created.append(Stamp)

first = created[0]()
second = created[0]()
print(created[0] is created[1])
print(type(first) is type(second))
