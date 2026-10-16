class Settings:
    def __init__(self, theme):
        self.theme = theme
    def __eq__(self, other):
        return self.theme == other.theme
    def __hash__(self):
        return len(self.theme)  # simple on purpose: equal themes have equal hashes

s = Settings("dark")
cache = {s: "rendered page"}
print("found:", s in cache)
original_hash = hash(s)

s.theme = "light"
print("hash changed:", hash(s) != original_hash)
print("but it is still in there:", len(cache))
