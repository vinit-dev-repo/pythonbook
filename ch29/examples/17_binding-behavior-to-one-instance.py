from types import MethodType

def greet(self):
    return f"hello, {self.name}"

class Member:
    say = greet                 # class storage: descriptor binding works

    def __init__(self, name):
        self.name = name
        self._registered = None

    def register(self, function):
        self._registered = MethodType(function, self)

    def perform(self):
        if self._registered is None:
            raise RuntimeError("no behavior registered")
        return self._registered()

def cheer(self):
    self.name += "!"
    return f"cheer: {self.name}"

def whisper(self):
    self.name += "?"
    return f"whisper: {self.name}"

ada = Member("Ada")
lin = Member("Lin")
print("class-bound:", ada.say())
ada.direct = greet
try:
    ada.direct()
except TypeError as error:
    print("instance function:", type(error).__name__)

ada.register(cheer)
lin.register(whisper)
print(ada.perform())
print(lin.perform())
print("receiver:", ada._registered.__self__ is ada)
print("function:", ada._registered.__func__ is cheer)
try:
    Member("Noor").perform()
except RuntimeError as error:
    print("missing:", error)
