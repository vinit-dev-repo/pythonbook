import abc


class ScoreCache(abc.ABC):
    @abc.abstractmethod
    def set(self, key, value):
        pass

    @abc.abstractmethod
    def get(self, key):
        pass


class InheritedScores(ScoreCache):
    def __init__(self):
        self._scores = {}

    def set(self, key, value):
        self._scores[key] = value

    def get(self, key):
        return self._scores[key]


class ExternalScores:
    def __init__(self):
        self._scores = {}

    def set(self, key, value):
        self._scores[key] = value

    def get(self, key):
        return self._scores[key]


class SingleSlotScores:
    def set(self, key, value):
        self._last = value

    def get(self, key):
        return self._last


ScoreCache.register(ExternalScores)
ScoreCache.register(SingleSlotScores)


def check_score_cache(cache):
    cache.set("Aisha", 95)
    assert cache.get("Aisha") == 95, "read after write"
    cache.set("Ben", 88)
    assert cache.get("Ben") == 88, "second write"
    assert cache.get("Aisha") == 95, "keys must keep separate values"
    cache.set("Aisha", 91)
    assert cache.get("Aisha") == 91, "replace a stored value"
    assert cache.get("Ben") == 88, "replacement must preserve other keys"


for cache in (InheritedScores(), ExternalScores(), SingleSlotScores()):
    print(type(cache).__name__, "ABC member:", isinstance(cache, ScoreCache))
    try:
        check_score_cache(cache)
    except AssertionError as error:
        print("behavior rejected:", error)
    else:
        print("shown behavior checks passed")
