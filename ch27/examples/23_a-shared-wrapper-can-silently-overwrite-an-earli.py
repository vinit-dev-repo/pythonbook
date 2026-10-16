def fresh_wrapper(cls):
    class Wrapper:
        def __init__(self, label):
            self.wrapped = cls(label)

    return Wrapper


@fresh_wrapper
class SafeCard:
    def __init__(self, label):
        self.label = label


@fresh_wrapper
class SafeBadge:
    def __init__(self, label):
        self.label = label


safe_one = SafeCard("first")
safe_two = SafeCard("second")
safe_badge = SafeBadge("blue")
print("fresh wrappers:", safe_one is safe_two, safe_one.wrapped.label, safe_two.wrapped.label)
print("separate repaired classes:", SafeCard is SafeBadge, safe_badge.wrapped.label)
