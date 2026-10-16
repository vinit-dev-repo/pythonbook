from dataclasses import dataclass, field

@dataclass(frozen=True)
class Team:
    name: str
    members: list = field(default_factory=list)

t = Team("A", ["Ana"])
t.members.append("Ben")      # frozen did not stop this
print(t)
