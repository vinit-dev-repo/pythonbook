def first_instance_cache(cls):
    first = None

    def build(*args, **kwargs):
        nonlocal first
        if first is None:
            first = cls(*args, **kwargs)
        return first

    return build


@first_instance_cache
class CachedDesk:
    def __init__(self, label):
        self.label = label


@first_instance_cache
class CachedShelf:
    def __init__(self, label):
        self.label = label


desk_first = CachedDesk("front")
desk_later = CachedDesk("ignored")
shelf_first = CachedShelf("top")
shelf_later = CachedShelf("ignored")
print("cache desk:", desk_first is desk_later, desk_later.label)
print("cache shelf:", shelf_first is shelf_later, shelf_later.label)
