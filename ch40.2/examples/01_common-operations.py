tags = {"python", "beginner"}
tags.add("tutorial")
print(sorted(tags))

tags.discard("nonexistent")   # silent, no error
print(sorted(tags))
