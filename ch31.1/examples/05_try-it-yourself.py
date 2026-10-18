# 1
def meow(self):
    return "Meow!"

Cat = type("Cat", (), {"meow": meow})
c = Cat()
print(c.meow())   # Meow!

# 2
def describe(self):
    return "point"

Point = type("Point", (), {"dims": 2, "describe": describe})
print(type(Point))
print(type(type))
print(Point().describe())

# 3
class Quiet:
    def __new__(cls):
        print("new")
        return super().__new__(cls)

    def __init__(self):
        print("init")

obj = Quiet()
print(isinstance(obj, Quiet), type(Quiet))
