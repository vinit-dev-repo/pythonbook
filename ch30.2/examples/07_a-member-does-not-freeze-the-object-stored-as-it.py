from enum import Enum

class Palette(Enum):
    DAY = ['cream']
    NIGHT = ['navy']

labels = {Palette.DAY: 'light theme'}
Palette.DAY.value.append('gold')
print(Palette.DAY.value)
print(labels[Palette.DAY])
for change in (
    lambda: setattr(Palette.DAY, 'value', ['new']),
    lambda: setattr(Palette, 'DAY', Palette.NIGHT),
):
    try:
        change()
    except AttributeError as error:
        print(type(error).__name__)
