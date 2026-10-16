class Label:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"Label({self.text!r})"

label = Label("north")
print(str(label))
print([label])
