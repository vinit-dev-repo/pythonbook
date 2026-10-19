team_a = ["Amy", "Ben", "Cara"]
team_b = ["Ben", "Dan", "Amy"]

in_both = set(team_a) & set(team_b)
only_in_a = set(team_a) - set(team_b)

print("In both teams:", sorted(in_both))
print("Only in team A:", sorted(only_in_a))
