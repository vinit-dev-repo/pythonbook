class BadLowerDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)

d = BadLowerDict()
d["Name"] = "Amy"            # goes through YOUR __setitem__ — works
print(d)

d.update({"CITY": "Paris"})  # update() is a dict METHOD — bypasses your override!
print(d)
