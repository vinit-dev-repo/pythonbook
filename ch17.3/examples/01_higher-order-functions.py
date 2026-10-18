words = ["banana", "kiwi", "apple"]
print(sorted(words, key=len))                       # sort by a function's result
print(list(map(str.upper, words)))                  # apply a function to every item
print(list(filter(lambda w: len(w) > 4, words)))     # keep items a function approves
