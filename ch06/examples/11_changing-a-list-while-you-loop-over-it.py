numbers = [1, 2, 4, 5]

for n in list(numbers):          # loop over a COPY
    if n % 2 == 0:
        numbers.remove(n)

print(numbers)
