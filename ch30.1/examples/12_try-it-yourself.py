from enum import Enum


# 1
class Season(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    AUTUMN = 4


print(Season.SPRING)
print(Season.SPRING.name, Season.SPRING.value)

# 2
print(Season["SUMMER"], Season(4))
for lookup in (lambda: Season["MONSOON"], lambda: Season(9)):
    try:
        lookup()
    except (KeyError, ValueError) as error:
        print(type(error).__name__)

# 3
for season in Season:
    print(season.name, season.value)
print(Season.WINTER == 1, Season.WINTER.value == 1, Season.AUTUMN is Season.AUTUMN)
