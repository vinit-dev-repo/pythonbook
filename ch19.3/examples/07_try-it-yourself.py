from collections import namedtuple

# 1
MinMax = namedtuple("MinMax", "low high")

def min_max(numbers):
    return MinMax(min(numbers), max(numbers))

print(min_max([4, 8, 15, 16, 23, 42]))   # MinMax(low=4, high=42)

# 2
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

independent_a = Bag("Ana", [])
independent_b = Bag("Bea", [])
independent_a.items.append("pen")
print(independent_a)
print(independent_b)
print(independent_a.items is independent_b.items)

# 3
Point3D = namedtuple("Point3D", "x y z", defaults=[0])
print(Point3D(1, 2))                  # Point3D(x=1, y=2, z=0)
print(Point3D(1, 2, 9))               # Point3D(x=1, y=2, z=9)

# 4
Point4D = namedtuple("Point4D", Point3D._fields + ("w",))
print(Point4D(1, 2, 3, 4))            # Point4D(x=1, y=2, z=3, w=4)

# 5
Stock = namedtuple("Stock", "code quantity")
incoming = {"quantity": 6, "code": "P-17"}
stock = Stock(**incoming)
print(stock._replace(quantity=8))     # Stock(code='P-17', quantity=8)
