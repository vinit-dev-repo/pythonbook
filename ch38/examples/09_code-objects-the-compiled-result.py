import dis

def add_tax(price, rate=0.1):
    total = price + price * rate
    return total

def count_up_to(n):
    num = 0
    while num < n:
        yield num
        num += 1

print("add_tax co_flags:", add_tax.__code__.co_flags)
print(dis.pretty_flags(add_tax.__code__.co_flags))
print()
print("count_up_to co_flags:", count_up_to.__code__.co_flags)
print(dis.pretty_flags(count_up_to.__code__.co_flags))
