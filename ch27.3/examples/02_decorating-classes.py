def add_label(cls):
    cls.label = "local class"
    return cls

class LabelledNote:
    pass

original_note_class = LabelledNote
LabelledNote = add_label(LabelledNote)

print(LabelledNote is original_note_class)
print(LabelledNote.label)
