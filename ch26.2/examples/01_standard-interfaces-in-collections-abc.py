from collections.abc import (
    Iterable, Iterator, Container, Sized, Sequence,
    MutableSequence, Mapping, Hashable, Callable,
)

abcs = [Iterable, Iterator, Container, Sized, Sequence,
        MutableSequence, Mapping, Hashable, Callable]

for abc_cls in abcs:
    print(abc_cls.__name__, sorted(abc_cls.__abstractmethods__))
