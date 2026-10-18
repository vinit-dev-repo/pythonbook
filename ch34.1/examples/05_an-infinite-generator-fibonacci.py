from itertools import islice

fib = fibonacci()
first_six = list(islice(fib, 6))
print(first_six)
