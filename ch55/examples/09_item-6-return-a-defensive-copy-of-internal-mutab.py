class GoodRoster:
    def __init__(self, names):
        self._names = list(names)    # defensive copy on the way in

    def get_names(self):
        return list(self._names)     # defensive copy on the way out

roster = GoodRoster(["Ana", "Ben"])
leaked = roster.get_names()
leaked.append("Intruder")
print(roster.get_names())            # untouched
