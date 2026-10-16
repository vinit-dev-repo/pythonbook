# 1
def is_even(n):
    return n % 2 == 0

print(is_even(4))    # True
print(is_even(7))    # False

# 2
def power(base, exponent=2):
    return base ** exponent

print(power(3))       # 9
print(power(2, 5))    # 32

# 3
def total(*numbers):
    return sum(numbers)

print(total(1, 2))            # 3
print(total(1, 2, 3))         # 6
print(total(1, 2, 3, 4, 5))   # 15

# 4
def add_score(score, scores=None):
    if scores is None:
        scores = []
    scores.append(score)
    return scores

print(add_score(10))   # [10]
print(add_score(20))   # [20]  -- not [10, 20], because it's a fresh list each time

# 5
words = ["kiwi", "fig", "banana", "apple"]
print(sorted(words, key=lambda word: len(word), reverse=True))
# ['banana', 'apple', 'kiwi', 'fig']
# Simpler equivalent: len is already the one-argument function we need.
print(sorted(words, key=len, reverse=True))   # ['banana', 'apple', 'kiwi', 'fig']

# 6
def summarize_scores(records, threshold=80):
    counts = {}
    qualifying = set()
    for name, score in records:
        counts[name] = counts.get(name, 0) + 1
        if score >= threshold:
            qualifying.add(name)
    return counts, sorted(qualifying)

records = [("Amara", 85), ("Ravi", 72), ("Amara", 91), ("Sam", 80)]
counts, names = summarize_scores(records)
print(counts)   # {'Amara': 2, 'Ravi': 1, 'Sam': 1}
print(names)    # ['Amara', 'Sam']
print(summarize_scores(records, threshold=91))
# ({'Amara': 2, 'Ravi': 1, 'Sam': 1}, ['Amara'])
print(summarize_scores([]))   # ({}, [])
print(records)  # original records, unchanged
