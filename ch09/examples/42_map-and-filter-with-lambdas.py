numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda n: n * 2, numbers))
print(doubled)

evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)
