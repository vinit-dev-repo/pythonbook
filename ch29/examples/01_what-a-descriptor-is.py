class Doorman:
    def __get__(self, instance, owner):
        print("Doorman: someone is reading the attribute")
        return "the value"

class House:
    front_door = Doorman()   # front_door is a descriptor, sitting on the CLASS

h = House()
print(h.front_door)
