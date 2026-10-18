class BrokenCache:
    def __init__(self):
        self._data = {}

    def get(self, key):
        return self._data.get(key)

    # oops - forgot to write set()

def remember_score(cache, name, score):
    cache.set(name, score)
    print(cache.get(name))

try:
    remember_score(BrokenCache(), "Ben", 88)
except AttributeError as e:
    print("AttributeError:", e)
