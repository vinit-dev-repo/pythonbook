# changing_bases.py
class DraftMode:
    def label(self):
        return "draft"

class PublishedMode:
    def label(self):
        return "published"

class DocumentMode(DraftMode):
    def label(self):
        return "document: " + super().label()

document = DocumentMode()
original_bases = DocumentMode.__bases__
print(document.label())
try:
    DocumentMode.__bases__ = (PublishedMode,)
    print(document.label())
    print([cls.__name__ for cls in DocumentMode.__mro__])
finally:
    DocumentMode.__bases__ = original_bases
print(document.label())

try:
    super()
except RuntimeError:
    print("zero-argument super needs method context")
