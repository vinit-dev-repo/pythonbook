# 1
def total(*numbers):
    return sum(numbers)

print(total(1, 2))            # 3
print(total(1, 2, 3))         # 6
print(total(1, 2, 3, 4, 5))   # 15

# 2
def show(**kwargs):
    for key in sorted(kwargs):
        print(key, "=", kwargs[key])

show(size="M", colour="red")  # colour = red, then size = M

# 3
def add(a, b, c):
    return a + b + c

nums = [4, 5, 6]
info = {"a": 1, "b": 2, "c": 3}
print(add(*nums))             # 15
print(add(**info))            # 6

# 4
def make_tag(text, *, bold=False):
    return "<b>" + text + "</b>" if bold else text

print(make_tag("hi", bold=True))   # <b>hi</b>
# make_tag("hi", True) raises TypeError: it takes 1 positional argument but 2 were given
