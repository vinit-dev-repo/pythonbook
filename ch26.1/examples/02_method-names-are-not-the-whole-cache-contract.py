class MemoryCache:
    def __init__(self):
        self._data = {}

    def get(self, key):
        return self._data.get(key)

    def set(self, key, value):
        self._data[key] = value

class SameShapeWrongCache:
    def get(self, key):
        return None

    def set(self, key, value):
        pass

def require_read_after_write(cache, key, value):
    cache.set(key, value)
    observed = cache.get(key)
    if observed != value:
        raise AssertionError(f"read-after-write expected {value!r}, got {observed!r}")

for cache in [MemoryCache(), SameShapeWrongCache()]:
    try:
        require_read_after_write(cache, "Aisha", 95)
    except AssertionError as error:
        print(type(cache).__name__, "rejected:", error)
    else:
        print(type(cache).__name__, "accepted for the shown case")
