# 1
temperature = 15
if temperature < 10:
    print("cold")
elif temperature < 25:
    print("mild")
else:
    print("hot")

# 2
for number in range(1, 20, 2):
    print(number)

# 3
count = 10
while count >= 1:
    print(count)
    count = count - 1
print("Liftoff!")

# 4
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        print(f"Stopped on {fruit}")
        break

# 5
for number in range(1, 21):
    if number % 3 == 0:
        continue
    print(number)

# 6
number = 7
label = "even" if number % 2 == 0 else "odd"
print(label)   # odd
