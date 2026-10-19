import inspect
import re
import reprlib

LABEL = re.compile(r"\b[A-Z]{2}-[0-9]{3}\b")


class StoredLabels:
    def __init__(self, text):
        self._text = text
        self._labels = LABEL.findall(text)

    def __getitem__(self, position):
        return self._labels[position]

    def __len__(self):
        return len(self._labels)

    def __repr__(self):
        return f"StoredLabels({reprlib.repr(self._text)})"


class YieldedLabels(StoredLabels):
    def __iter__(self):
        for label in self._labels:
            yield label


class LazyLabels:
    def __init__(self, text):
        self._text = text

    def __iter__(self):
        for match in LABEL.finditer(self._text):
            yield match.group()


class ExpressionLabels(LazyLabels):
    def __iter__(self):
        return (match.group() for match in LABEL.finditer(self._text))


text = "AA-103, BB-207; AA-103"
for kind in (StoredLabels, YieldedLabels, LazyLabels, ExpressionLabels):
    labels = kind(text)
    first, second = iter(labels), iter(labels)
    assert first is not second
    print(kind.__name__, next(first), list(second), list(first))

print("generator methods:", [
    inspect.isgeneratorfunction(kind.__iter__)
    for kind in (YieldedLabels, LazyLabels, ExpressionLabels)
])
