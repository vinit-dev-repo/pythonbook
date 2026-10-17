# 1
red_team = {"amara", "ravi", "sam"}
blue_team = {"sam", "lee"}
print(sorted(red_team & blue_team))      # on both teams
print(sorted(red_team ^ blue_team))      # on exactly one team

# 2
print(sorted(set([3, 1, 3, 2, 1])))      # [1, 2, 3]

# 3
weekdays = {"Mon", "Tue"}
week = {"Mon", "Tue", "Wed"}
print(weekdays <= week)                  # True

# 4
# (a) a tuple: a fixed record of ordered items
# (b) a dict: the names are the keys, the numbers are the values
# (c) a set: it keeps only unique items
