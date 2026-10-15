# tombola.py
import abc


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """Add all values from a finite iterable."""

    @abc.abstractmethod
    def pick(self):
        """Remove and return one value, or raise LookupError when empty."""

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
