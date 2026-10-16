literal = {"a", "b", "c"}
from_list = set([1, 2, 2, 3, 3, 3])      # duplicates vanish — a dedup idiom
from_string = set("hello")               # iterates the characters
empty = set()                            # NOT {} — see the trap below

print(sorted(literal))
print(sorted(from_list))
print(sorted(from_string))
print(empty)
