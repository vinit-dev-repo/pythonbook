# 1
class Echo:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return "instance"


class Box:
    item = Echo()


print(Box().item)
print(Box.item is vars(Box)["item"])


# 2
class Locked:
    def __get__(self, instance, owner):
        return "descriptor wins"

    def __set__(self, instance, value):
        pass


class Demo:
    x = Locked()


d = Demo()
d.__dict__["x"] = 99
print(d.x)

# 3
box = Box()
box.__dict__["item"] = "from the instance"
print(box.item)
