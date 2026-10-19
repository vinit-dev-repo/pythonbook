class DictCache:
    def __init__(self):
        self._data = {}

    def get(self, key):
        return self._data.get(key)

    def set(self, key, value):
        self._data[key] = value


class ListLoggingCache:
    """No shared application-specific base with DictCache."""
    def __init__(self):
        self._log = []

    def get(self, key):
        self._log.append(("get", key))
        return "(would ask the real store)"

    def set(self, key, value):
        self._log.append(("set", key, value))


def remember_score(cache, name, score):
    cache.set(name, score)
    print(cache.get(name))


for cache in [DictCache(), ListLoggingCache()]:
    remember_score(cache, "Aisha", 95)
