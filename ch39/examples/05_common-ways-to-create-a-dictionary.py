literal = {"apple": 1.20, "banana": 0.50}
from_kwargs = dict(apple=1.20, banana=0.50)
from_pairs = dict([("apple", 1.20), ("banana", 0.50)])
same_start = dict.fromkeys(["apple", "banana"], 0)
names = ["apple", "banana"]
prices = [1.20, 0.50]
from_zip = dict(zip(names, prices))
from_comp = {n: p for n, p in zip(names, prices)}

print(literal)
print(same_start)
print(from_zip)
