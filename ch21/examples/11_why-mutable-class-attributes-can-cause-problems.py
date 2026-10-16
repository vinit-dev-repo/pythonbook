class Team:
    def __init__(self, name):
        self.name = name
        self.members = []   # create a separate list for this object

    def add_member(self, person):
        self.members.append(person)

team_a = Team("Red")
team_b = Team("Blue")
team_a.add_member("Asha")
print(team_a.members)
print(team_b.members)
