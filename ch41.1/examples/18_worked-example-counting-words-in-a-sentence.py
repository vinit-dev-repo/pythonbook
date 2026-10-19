text = "the cat sat on the mat the cat ran"
word_counts = Counter(text.split())
print(word_counts.most_common(2))
