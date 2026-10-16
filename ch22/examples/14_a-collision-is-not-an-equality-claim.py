class CollisionKey:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if type(other) is not CollisionKey:
            return NotImplemented
        return self.value == other.value

    def __hash__(self):
        return 7

a = CollisionKey("a")
b = CollisionKey("b")
print(a == b)
print(hash(a) == hash(b))
print(len({a, b}))
