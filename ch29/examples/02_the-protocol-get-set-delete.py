class Doorman:
    def __get__(self, instance, owner):
        print(f"__get__ called. instance is a {type(instance).__name__}, owner={owner.__name__}")
        return 42

    def __set__(self, instance, value):
        print(f"__set__ called. instance is a {type(instance).__name__}, value={value}")

class House:
    front_door = Doorman()

h = House()
h.front_door           # read
h.front_door = "key"   # write
