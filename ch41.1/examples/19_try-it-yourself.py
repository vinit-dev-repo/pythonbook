from collections import Counter, OrderedDict, defaultdict

# 1
scores = [("Amy", 90), ("Leo", 75), ("Amy", 85)]
by_name = defaultdict(list)
for name, score in scores:
    by_name[name].append(score)
print(dict(by_name))

# 2
letters = Counter("mississippi")
print(letters.most_common(1))

# 3
d = defaultdict(int)
print("typo" in d, list(d))
if d["typo"] > 0:
    pass
print(list(d))

# 4
a = Counter(apple=3, banana=2)
b = Counter(apple=1, banana=4, cherry=1)
print(dict(a - b))
balance = a.copy()
balance.subtract(b)
print(dict(balance))

# 5
queue = OrderedDict(first=1, second=2, third=3)
queue.move_to_end("first")
print(list(queue))
print(queue.popitem(last=False))
print(OrderedDict(a=1, b=2) == OrderedDict(b=2, a=1), OrderedDict(a=1, b=2) == {"b": 2, "a": 1})
