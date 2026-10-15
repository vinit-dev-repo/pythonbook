# light_levels.py
import reprlib


class LightLevels:
    __slots__ = ("_levels",)

    def __init__(self, levels):
        values = tuple(levels)
        if any(type(value) is not int for value in values):
            raise TypeError("levels must be built-in integers")
        if any(not 0 <= value <= 100 for value in values):
            raise ValueError("levels must be between 0 and 100")
        object.__setattr__(self, "_levels", values)

    def __setattr__(self, name, value):
        raise AttributeError("light levels cannot be changed")

    def __delattr__(self, name):
        raise AttributeError("light levels cannot be deleted")

    def __len__(self):
        return len(self._levels)

    def __iter__(self):
        return iter(self._levels)

    def __getitem__(self, index):
        result = self._levels[index]
        return type(self)(result) if isinstance(index, slice) else result

    def __getattr__(self, name):
        positions = {"first": 0, "last": -1}
        if name in positions and self._levels:
            return self._levels[positions[name]]
        raise AttributeError(name)

    def __eq__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return len(self) == len(other) and all(
            left == right for left, right in zip(self, other)
        )

    def __hash__(self):
        return hash(self._levels)

    def __repr__(self):
        return f"{type(self).__name__}({reprlib.repr(self._levels)})"

    def __bytes__(self):
        return b"LV1" + bytes(self._levels)

    @classmethod
    def from_bytes(cls, data):
        if not isinstance(data, bytes):
            raise TypeError("data must be bytes")
        if not data.startswith(b"LV1"):
            raise ValueError("unknown level format")
        return cls(data[3:])

    def __format__(self, spec):
        if spec.startswith("mean;"):
            if not self:
                raise ValueError("an empty series has no mean")
            return "mean=" + format(sum(self) / len(self), spec[5:])
        return "[" + " / ".join(format(value, spec) for value in self) + "]"


if __name__ == "__main__":
    source = [12, 30, 18]
    levels = LightLevels(source)
    source[0] = 99
    print(levels.first, levels.last, list(reversed(levels)))
    print(repr(levels[::2]))
    restored = LightLevels.from_bytes(bytes(levels))
    print(restored == levels, hash(restored) == hash(levels))
    print(len({levels, restored}), levels == [12, 30, 18])
    print(f"{levels:03d}", f"{levels:mean;.1f}")
    print(list(bytes(levels)), bool(LightLevels([])))
