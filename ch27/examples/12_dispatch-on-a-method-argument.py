from functools import singledispatchmethod

class Receipt:
    def __init__(self, label):
        self.label = label

    @singledispatchmethod
    def render(self, value):
        return f"{self.label}: unsupported {type(value).__name__}"

    @render.register(int)
    def _(self, value):
        return f"{self.label}: count {value}"

    @render.register(str)
    def _(self, value):
        return f"{self.label}: note {value}"

front = Receipt("front")
back = Receipt("back")
print(front.render(4))
print(back.render("ready"))
print(front.render(2.5))
print(front.render(True))
