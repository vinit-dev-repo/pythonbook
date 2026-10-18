import collections.abc


# 1
class EmailNotifier:
    def send(self, message):
        return f"emailed: {message}"


class SmsNotifier:
    def send(self, message):
        return f"texted: {message}"


def announce(notifier, message):
    print(notifier.send(message))


for notifier in [EmailNotifier(), SmsNotifier()]:
    announce(notifier, "build finished")


# 2
class Basket:
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)


print(isinstance(Basket(), collections.abc.Sized))


# 3
class Countdown:
    def __getitem__(self, index):
        if not 0 <= index <= 3:
            raise IndexError(index)
        return 3 - index


print(list(Countdown()))
print(2 in Countdown())
print(isinstance(Countdown(), collections.abc.Iterable))
