class Odd:
    def __new__(cls):
        return 42                                 # not an Odd
    def __init__(self):
        raise RuntimeError("this never runs")

print(Odd())
print(type(Odd()).__name__)
