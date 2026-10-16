class CleanedField:
    """Store the value returned by a subclass's normalize hook."""
    def __set_name__(self, owner, name):
        self.name, self.storage = name, "_" + name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        if self.storage not in instance.__dict__:
            raise AttributeError(self.name)
        return instance.__dict__[self.storage]

    def normalize(self, value):
        raise NotImplementedError("supply a normalization rule")

    def __set__(self, instance, value):
        accepted = self.normalize(value)
        instance.__dict__[self.storage] = accepted

class WordLabel(CleanedField):
    """Require built-in text with at least one non-whitespace word."""
    def normalize(self, value):
        if type(value) is not str:
            raise TypeError("label must be built-in text")
        cleaned = " ".join(value.split())
        if not cleaned:
            raise ValueError("label must contain a word")
        return cleaned

class Exhibit:
    label = WordLabel()

exhibit = Exhibit()
exhibit.label = "  Early   tools  "
print(exhibit.label)
try:
    exhibit.label = "   "
except ValueError:
    print("retained:", exhibit.label)
print(Exhibit.label.__doc__)
