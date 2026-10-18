# 1
class Position:
    def __init__(self, value):
        self.value = value

    def __index__(self):
        return self.value

print("ABCDE"[Position(3)])                    # D
print("ABCDE"[Position(1):Position(3)])        # BC
print(bin(Position(5)))                        # 0b101

# 2
class OnlyInt:
    def __int__(self):
        return 2

print(int(OnlyInt()))                          # 2
try:
    print("ABCDE"[OnlyInt()])
except TypeError as error:
    print(type(error).__name__)                # TypeError
