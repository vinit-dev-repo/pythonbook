class BadRoster:
    def __init__(self, names):
        self._names = names          # stores the caller's list directly

    def get_names(self):
        return self._names           # hands out the real internal list

roster = BadRoster(["Ana", "Ben"])
leaked = roster.get_names()
leaked.append("Intruder")            # looks like it only changes "leaked"...
print(roster.get_names())            # ...but the roster changed too!
