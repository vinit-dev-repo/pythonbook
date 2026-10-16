d = defaultdict(int)
if d["typo"] > 0:      # this ALSO created "typo" as a side effect!
    pass
print(list(d.keys()))
