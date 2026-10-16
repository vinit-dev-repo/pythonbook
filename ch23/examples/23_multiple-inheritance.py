class Swimmer:
    def move(self):
        return "swims"

class Walker:
    def move(self):
        return "walks"

class Beaver(Swimmer, Walker):
    pass

b = Beaver()
print(b.move())
print(Beaver.__mro__)
