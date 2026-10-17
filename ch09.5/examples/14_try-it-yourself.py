# 1
words = ["kiwi", "fig", "banana", "apple"]
print(sorted(words, key=lambda word: len(word), reverse=True))
# ['banana', 'apple', 'kiwi', 'fig']
# Simpler equivalent: len is already the one-argument function we need.
print(sorted(words, key=len, reverse=True))   # ['banana', 'apple', 'kiwi', 'fig']

# 2
nums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda n: n * n, filter(lambda n: n % 2 == 0, nums))))   # [4, 16, 36]
print([n * n for n in nums if n % 2 == 0])                              # [4, 16, 36]

# 3
print(round(0.5), round(1.5), round(2.5))   # 0 2 2: ties go to the even neighbour
print(min(words, key=len), max(words, key=len))   # fig banana

# 4
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
