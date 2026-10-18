from enum import Enum

class DescribableEnum(Enum):
    def describe(self):
        return f"{self.name} ({self.value})"

class Color(DescribableEnum):
    RED = 1
    GREEN = 2

class Size(DescribableEnum):
    SMALL = "S"
    LARGE = "L"

print(Color.RED.describe())
print(Size.LARGE.describe())
