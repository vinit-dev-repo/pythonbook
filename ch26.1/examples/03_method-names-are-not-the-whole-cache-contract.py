class Always95Cache:
    def get(self, key):
        return 95

    def set(self, key, value):
        pass


def require_read_after_write(cache, key, value):
    cache.set(key, value)
    observed = cache.get(key)
    if observed != value:
        raise AssertionError(f"read-after-write expected {value!r}, got {observed!r}")


cache = Always95Cache()
require_read_after_write(cache, "Aisha", 95)
print("shown case accepted")

try:
    require_read_after_write(cache, "Ben", 88)
except AssertionError as error:
    print("transfer rejected:", error)
