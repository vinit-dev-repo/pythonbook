note = Note()
print(getattr(note, "title"))
print(getattr(note, "color", "no color"))
setattr(note, "color", "teal")
print(note.color)
delattr(note, "color")
try:
    print(note.color)
except AttributeError as error:
    print(type(error).__name__)
try:
    print(vars(note)["color"])
except KeyError as error:
    print(type(error).__name__)
