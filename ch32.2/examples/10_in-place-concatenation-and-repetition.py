word = "cat"
before_id = id(word)
word += "s"
after_id = id(word)
print(word)
print(before_id == after_id)   # DIFFERENT object
