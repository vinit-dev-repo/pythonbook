class PretendsToBeInt:
    @property
    def __class__(self):
        return int

item = PretendsToBeInt()
print(type(item) is PretendsToBeInt)
print(item.__class__ is int)
print(isinstance(item, int))
