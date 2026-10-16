print(hash(42))                             # int — fine, and predictable: same every run
print(hash("hello") == hash("hello"))       # str — fine, and stable within THIS run
print(hash((1, 2, 3)) == hash((1, 2, 3)))   # tuple — fine, because its contents don't change
print(hash([1, 2, 3]))                      # list — NOT fine
