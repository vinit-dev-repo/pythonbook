# 1
from collections import defaultdict
scores = [("Amy", 90), ("Leo", 75), ("Amy", 85)]
by_name = defaultdict(list)
for name, score in scores:
    by_name[name].append(score)
print(dict(by_name))    # {'Amy': [90, 85], 'Leo': [75]}

# 2
from collections import Counter
letters = Counter("mississippi")
print(letters.most_common(1))   # [('i', 4)]

# 3
from collections import ChainMap
user_prefs = {"volume": 90}
defaults = {"volume": 50, "brightness": 70}
settings = ChainMap(user_prefs, defaults)
print(settings["volume"])       # 90 — from user_prefs
print(settings["brightness"])   # 70 — from defaults

# 4
# dict.update can bypass an overridden setter. UserDict.update uses it.
# In this version, UserDict in-place union updates .data directly.
# Define the supported operations, then test each required path.

# 5
from types import MappingProxyType
stock = {"apples": 10}
public_stock = MappingProxyType(stock)
stock["apples"] = 3
print(public_stock["apples"])   # 3 — live view, sees the change
try:
    public_stock["apples"] = 99
except TypeError as e:
    print("Blocked:", e)
