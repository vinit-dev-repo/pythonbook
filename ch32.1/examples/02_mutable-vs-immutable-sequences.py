numbers = [10, 20, 30]
numbers[1] = 99        # calls __setitem__
del numbers[0]          # calls __delitem__
print(numbers)
