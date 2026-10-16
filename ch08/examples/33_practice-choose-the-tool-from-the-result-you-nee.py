labels = ["bay-2", "bay-1", "bay-2"]
number = 1
wanted = "bay-" + str(number)

position = 0
while position < len(labels):
    if labels[position] == wanted:
        print("while position:", position)
        break
    position += 1
else:
    print("while: absent")

for position, label in enumerate(labels):
    if label == wanted:
        print("for position:", position)
        break
else:
    print("for: absent")

print("present:", wanted in labels)
print("generated labels:", ["bay-" + str(n) for n in range(1, 4)])
