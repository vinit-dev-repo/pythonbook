from tracer_lab import Tracer

class BaseLabel:
    def __init__(self, text):
        self.text = text

    def show(self):
        return self.text.upper()

@Tracer
class Label(BaseLabel):
    pass

item = Label("go")
print(item.show())
print(isinstance(item, Label))
