class SharedWrapper:
    def __init__(self, cls):
        self.cls = cls
        self.wrapped = None

    def __call__(self, label):
        self.wrapped = self.cls(label)
        return self


@SharedWrapper
class BrokenCard:
    def __init__(self, label):
        self.label = label


@SharedWrapper
class BrokenBadge:
    def __init__(self, label):
        self.label = label


first_card = BrokenCard("first")
second_card = BrokenCard("second")
badge = BrokenBadge("blue")
print("shared card:", first_card is second_card, first_card.wrapped.label)
print("separate class decorators:", BrokenCard is BrokenBadge, badge.wrapped.label, first_card.wrapped.label)
