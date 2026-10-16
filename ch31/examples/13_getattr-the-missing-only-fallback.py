class Proxy:
    def __init__(self, target):
        self._target = target

    def __getattr__(self, name):
        print(f"'{name}' not found directly -- forwarding to target")
        return getattr(self._target, name)

class RealThing:
    def greet(self):
        return "Hello from the real thing"

p = Proxy(RealThing())
print(p.greet())
