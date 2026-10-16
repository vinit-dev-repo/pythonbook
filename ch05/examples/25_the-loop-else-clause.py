numbers = [2, 4, 5, 8]

for number in numbers:
    if number % 2 != 0:
        print("Found an odd number!")
        break
else:
    print("All numbers were even.")
