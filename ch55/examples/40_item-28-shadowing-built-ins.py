list = [1, 2, 3]     # shadows the built-in list() type
print(list)
# list("abc")  # would now crash: TypeError, 'list' object is not callable
