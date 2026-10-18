class Team:
    members = []   # one shared list for every Team instance

    def __init__(self, name):
        self.name = name

    def add_member(self, person):
        self.members.append(person)

team_a = Team("Red")
team_b = Team("Blue")
team_a.add_member("Asha")
print(team_b.members)
