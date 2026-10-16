numbers = [1, 2, 3, 4, 5, 6]

# map() + filter(), with a separate function
def is_even(n):
    return n % 2 == 0

def double(n):
    return n * 2

result = list(map(double, filter(is_even, numbers)))
print(result)
