from collections.abc import Hashable, Sized

class BrokenLength:
    __len__ = 3

tuple_with_list = ([],)
print(isinstance(tuple_with_list, Hashable))
try:
    hash(tuple_with_list)
except TypeError as error:
    print(type(error).__name__)

print(isinstance(BrokenLength(), Sized))
try:
    len(BrokenLength())
except TypeError as error:
    print(type(error).__name__)
