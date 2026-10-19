from collections import defaultdict

scores = defaultdict(int)   # int() with no arguments gives 0
scores["alice"] += 10
scores["bob"] += 5
print(scores["carol"])      # never mentioned before — no error!
print(scores)
