# 26.1 - Interfaces, Duck Typing and Goose Typing

The code of the chapter **26.1 - Interfaces, Duck Typing and Goose Typing** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What an interface is in Python, which has no `interface` keyword
- How duck typing works, and why a missing-method error can arrive late
- How a class with only `__getitem__` still works in a `for` loop
- What goose typing is: `isinstance` against an abstraction instead of a concrete class

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_duck-typing-use-operations-without-checking-a-cl.py` | Duck typing: use operations without checking a class (line 59) | runs on its own |
| `examples/02_method-names-are-not-the-whole-cache-contract.py` | Duck typing: use operations without checking a class › Method names are not the whole cache contract (line 107) | runs on its own |
| `examples/03_method-names-are-not-the-whole-cache-contract.py` | Duck typing: use operations without checking a class › Method names are not the whole cache contract (line 156) | runs on its own |
| `examples/04_the-exact-weakness-errors-arrive-late.py` | Duck typing: use operations without checking a class › The exact weakness: errors arrive late (line 193) | runs on its own |
| `examples/05_python-s-own-duck-typing-trick-the-sequence-prot.py` | Duck typing: use operations without checking a class › Python's own duck typing trick: the sequence protocol (line 229) | runs on its own |
| `examples/06_iteration-can-succeed-without-iterable-recogniti.py` | Duck typing: use operations without checking a class › Iteration can succeed without `Iterable` recognition (line 268) | may use names from earlier examples |
| `examples/07_iteration-can-succeed-without-iterable-recogniti.py` | Duck typing: use operations without checking a class › Iteration can succeed without `Iterable` recognition (line 301) | may use names from earlier examples |
| `examples/08_goose-typing-isinstance-against-an-abstraction.py` | Goose typing: `isinstance` against an abstraction (line 329) | runs on its own |
| `examples/09_try-it-yourself.py` | Try it yourself (line 384) | runs on its own |
