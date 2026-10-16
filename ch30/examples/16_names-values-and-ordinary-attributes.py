from enum import Enum

class Reading(Enum):
    HIGH = 40
    LOW = 10

    def describe(self):
        return self.name.lower()

print([item.value for item in Reading])
print(Reading.__members__['HIGH'] is Reading.HIGH)
print('describe' in Reading.__members__, hasattr(Reading, 'describe'))
print(40 in Reading, isinstance(40, Reading))
print(Reading.HIGH.describe())
try:
    Reading.__members__['MID'] = Reading.HIGH
except TypeError as error:
    print(type(error).__name__)
Reading.note = 'display only'
print(Reading.note, 'note' in Reading.__members__)
