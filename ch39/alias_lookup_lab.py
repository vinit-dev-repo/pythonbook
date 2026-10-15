# alias_lookup_lab.py
class AliasLookup(dict):
    aliases = {"n": "north", "s": "south"}

    def __missing__(self, key):
        target = self.aliases.get(key, key)
        if not dict.__contains__(self, target):
            raise KeyError(key)
        return dict.__getitem__(self, target)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return (dict.__contains__(self, key)
                or dict.__contains__(self, self.aliases.get(key, key)))

rooms = AliasLookup(north=4, south=2)
print(rooms["n"], rooms.get("s"), "n" in rooms)
print(rooms.get("west", 0), "west" in rooms)
try:
    rooms["west"]
except KeyError:
    print("missing without recursion")
rooms["n"] = 9
print(rooms["n"], rooms["north"])
print(list(rooms))
