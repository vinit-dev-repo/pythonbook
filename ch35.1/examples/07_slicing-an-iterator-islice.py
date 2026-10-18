import itertools

def all_powers_of_two():
    n = 1
    while True:
        yield n
        n *= 2

first_six = itertools.islice(all_powers_of_two(), 6)
print(list(first_six))
