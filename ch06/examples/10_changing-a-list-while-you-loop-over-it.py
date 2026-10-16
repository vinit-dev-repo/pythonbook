numbers = [1, 2, 4, 5]
kept = []
for n in numbers:
    if n % 2 != 0:
        kept.append(n)
numbers = kept
print(numbers)
