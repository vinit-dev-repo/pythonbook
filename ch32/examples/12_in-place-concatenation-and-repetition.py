numbers = [1, 2, 3]
before_id = id(numbers)
numbers += [4, 5]
after_id = id(numbers)
print(numbers)
print(before_id == after_id)   # SAME object — it grew in place
