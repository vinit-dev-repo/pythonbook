# 1
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        print(f"Stopped on {fruit}")
        break

# 2
for number in range(1, 21):
    if number % 3 == 0:
        continue
    print(number)

# 3
for number in [2, 4, 6]:
    if number % 2 != 0:
        print("Found an odd number!")
        break
else:
    print("no odd number")   # no break ran, so the else block runs
