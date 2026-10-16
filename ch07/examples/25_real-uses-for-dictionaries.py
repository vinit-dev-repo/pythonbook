text = "the cat sat on the mat the cat ran"
counts = {}

for word in text.split():
    counts[word] = counts.get(word, 0) + 1       # adds a new key (if key doesn't exist), or at the same time updates the value of existing key
    print(counts)
print(counts)
