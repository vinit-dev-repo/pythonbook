class NoEq:
    def __init__(self, value):
        self.value = value

a = NoEq(5)
b = NoEq(5)
print(a == b)
