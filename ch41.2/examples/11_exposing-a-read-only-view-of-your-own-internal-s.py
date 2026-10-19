class Settings:
    def __init__(self):
        self._data = {"volume": 80, "brightness": 50}
        self.public = MappingProxyType(self._data)   # shallow read-only view of the mapping

    def set_volume(self, value):
        self._data["volume"] = value   # change through the intended public method

s = Settings()
print(s.public["volume"])
s.set_volume(60)
print(s.public["volume"])    # sees the change — it's a live view

try:
    s.public["volume"] = 100   # outsiders cannot change it directly
except TypeError as e:
    print("Blocked:", e)
