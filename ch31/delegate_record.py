# delegate_record.py
class Client:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"hello, {self.name}"

    def __repr__(self):
        return f"Client({self.name!r})"

class ClientView:
    def __init__(self, target):
        self.target = target

    def __getattr__(self, name):
        return getattr(self.target, name)

    def __repr__(self):
        return f"ClientView({self.target!r})"

if __name__ == "__main__":
    target = Client("Ada")
    view = ClientView(target)
    method = view.greet
    print("method target:", method.__self__ is target)
    print(method())
    view.name = "view-only"
    print("wrapper name:", view.name)
    print("target name:", target.name)
    print(repr(view))
