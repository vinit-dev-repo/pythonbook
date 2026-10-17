words = ["cat", "dog", "cat", "bird", "dog"]
unique_lengths = {len(word) for word in words}
print(sorted(unique_lengths))
