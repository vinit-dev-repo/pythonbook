words = ["banana", "fig", "apple", "kiwi"]
print(sorted(words, key=len))               # sort by LENGTH, not alphabet
print(sorted(words, key=str.upper))          # sort ignoring case
print(sorted(words, key=len, reverse=True))  # longest first
