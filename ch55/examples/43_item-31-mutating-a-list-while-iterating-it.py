numbers = [1, 2, 4, 6, 3, 5]

# buggy — removing 2 shifts 4 into the position already visited
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)
print(numbers)
