# 1
for number in range(1, 20, 2):
    print(number)

# 2
count = 10
while count >= 1:
    print(count)
    count = count - 1
print("Liftoff!")

# 3
shopping = ["bread", "milk", "eggs"]
for number, item in enumerate(shopping, start=1):
    print(f"{number}. {item}")
