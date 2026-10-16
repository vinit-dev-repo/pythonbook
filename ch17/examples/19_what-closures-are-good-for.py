# A running-total accumulator
def make_accumulator():
    total = 0
    def add(amount):
        nonlocal total
        total += amount
        return total
    return add

running_total = make_accumulator()
print(running_total(10))
print(running_total(5))
print(running_total(20))
