numbers = [1, 2, 4, 5]

for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)        # changing the list while looping over it

print(numbers)
