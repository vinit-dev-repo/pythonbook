from functools import reduce

numbers = [3, 7, 2, 9, 4]

my_sum = reduce(lambda acc, n: acc + n, numbers, 0)
my_max = reduce(lambda acc, n: acc if acc > n else n, numbers)

print(my_sum)
print(my_max)
