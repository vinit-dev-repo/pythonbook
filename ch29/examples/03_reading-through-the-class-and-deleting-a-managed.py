class ManagedDoor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        try:
            return instance.__dict__["_door"]
        except KeyError:
            raise AttributeError("front_door is not set") from None

    def __set__(self, instance, value):
        instance.__dict__["_door"] = value

    def __delete__(self, instance):
        try:
            del instance.__dict__["_door"]
        except KeyError:
            raise AttributeError("front_door is not set") from None

class House:
    front_door = ManagedDoor()

h = House()
h.front_door = "open"
print(h.front_door)
print(House.front_door is vars(House)["front_door"])
del h.front_door
try:
    print(h.front_door)
except AttributeError as error:
    print(type(error).__name__ + ":", error)
h.spare = vars(House)["front_door"]
print(h.spare is House.front_door)
