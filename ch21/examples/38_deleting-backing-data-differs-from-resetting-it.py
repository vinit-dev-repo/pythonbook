class Cell:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @value.deleter
    def value(self):
        del self._value

cell = Cell(10)
print(getattr(cell, "value"))
delattr(cell, "value")
try:
    print(cell.value)
except AttributeError as error:
    print(type(error).__name__)
print(isinstance(Cell.value, property))
setattr(cell, "value", 20)
print(cell.value)
