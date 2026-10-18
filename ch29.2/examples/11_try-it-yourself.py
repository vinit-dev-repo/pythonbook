# 1 and 2
class NonEmptyString:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.private_name not in instance.__dict__:
            raise AttributeError(self.private_name[1:])
        return instance.__dict__[self.private_name]

    def __set__(self, instance, value):
        if type(value) is not str:
            raise TypeError("must be a built-in string")
        if value == "":
            raise ValueError("must not be empty")
        instance.__dict__[self.private_name] = value


class Book:
    title = NonEmptyString()

    def __init__(self, title):
        self.title = title


b = Book("Dune")
print(b.title)
try:
    Book("")
except ValueError as error:
    print(error)

# 3
# Because self.value lives on the ONE shared PositiveNumber object,
# not on each Product instance: every Product reads and writes the same slot.
