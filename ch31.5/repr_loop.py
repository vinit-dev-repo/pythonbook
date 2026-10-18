# repr_loop.py
class RecursiveDisplay:
    def action(self):
        pass

    def __repr__(self):
        return repr(self.action)

try:
    repr(RecursiveDisplay())
except RecursionError:
    print("bound method display called the object's repr again")

class SafeDisplay(RecursiveDisplay):
    def __repr__(self):
        return f"SafeDisplay(method={self.action.__func__.__name__})"

print(repr(SafeDisplay()))
