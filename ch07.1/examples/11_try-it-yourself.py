# 1
ages = {"amara": 21, "ravi": 24}
ages["sam"] = 19
print(ages)                  # {'amara': 21, 'ravi': 24, 'sam': 19}

# 2
print(ages.get("lee", "unknown"))   # unknown

# 3
removed = ages.pop("ravi")
print(removed)               # 24
print(ages)                  # {'amara': 21, 'sam': 19}
