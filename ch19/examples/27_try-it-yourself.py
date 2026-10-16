# 5
Bag = namedtuple("Bag", "owner items", defaults=[[]])
a = Bag("Ana")
b = Bag("Bea")
a.items.append("pen")
c = a._replace(owner="Cal")
print(a)
print(b)
print(c)
print(a is b, a is c)
print(a.items is b.items, a.items is c.items)

# Start a fresh independent pair; each [] is a new list.
independent_a = Bag("Ana", [])
independent_b = Bag("Bea", [])
independent_a.items.append("pen")
print(independent_a)
print(independent_b)
print(independent_a.items is independent_b.items)
