import itertools

morning = ["porridge", "toast"]
evening = ["pasta", "salad"]

meals = itertools.chain(morning, evening)
print(list(meals))
