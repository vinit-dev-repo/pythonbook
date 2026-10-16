import sys

numbers = [1, 2, 3]
also_numbers = numbers          # a second name tag, same list
print(sys.getrefcount(numbers))
