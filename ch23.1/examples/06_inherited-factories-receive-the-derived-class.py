class NamedRecord:
    category = "record"

    def __init__(self, name):
        self.name = name

    def categories(self):
        return self.category, NamedRecord.category, type(self).category

    @classmethod
    def from_text(cls, text):
        print("factory:", cls.__name__)
        return cls(text.strip())

class TaggedRecord(NamedRecord):
    category = "tagged"

first = TaggedRecord.from_text(" Ana ")
second = first.from_text(" Bea ")
print(type(first).__name__, first.name)
print(type(second).__name__, second.name)
first.category = "personal"
print(first.category, second.category, TaggedRecord.category)
print(first.categories())
