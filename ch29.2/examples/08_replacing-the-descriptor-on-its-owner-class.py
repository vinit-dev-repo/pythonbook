class Controlled:
    def __get__(self, instance, owner=None):
        return self if instance is None else "managed read"

    def __set__(self, instance, value):
        raise ValueError("managed assignment")

class Panel:
    state = Controlled()

panel = Panel()
saved = Panel.state
panel.__dict__["state"] = "instance entry"
print(panel.state)
Panel.state = "class replacement"
print(panel.state)
print(Panel().state)
Panel.state = saved
print(panel.state)
