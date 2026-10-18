def show_owner(self):
    return self.owner

class Label:
    def __init__(self, owner):
        self.owner = owner

label = Label("Asha")
label.show_owner = show_owner
try:
    label.show_owner()
except TypeError as error:
    print(type(error).__name__)
print(label.show_owner(label))

del label.show_owner
Label.show_owner = show_owner
print(label.show_owner())
