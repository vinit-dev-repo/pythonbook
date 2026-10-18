from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    def describe(self):
        return f"{self.name} is color number {self.value}"

print(Color.RED.describe())
