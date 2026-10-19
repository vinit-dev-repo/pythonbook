# 37.1 - Reference Counts, Cycles and Weak References

The code of the chapter **37.1 - Reference Counts, Cycles and Weak References** of the Python tutorial (folder `05 - Runtime`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Explain CPython reference counts and unreachable reference cycles.
- Observe an object through a weak reference, a finalizer and a weak set without owning it.
- Tell which classes support weak references.

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_reference-counting-in-cpython.py` | Reference counting in CPython (line 48) | runs on its own |
| `examples/02_reference-counting-in-cpython.py` | Reference counting in CPython (line 61) | may use names from earlier examples |
| `examples/03_when-the-count-hits-zero.py` | Reference counting in CPython › When the count hits zero (line 78) | may use names from earlier examples |
| `examples/04_the-problem-reference-counting-cannot-solve-on-i.py` | Reference counting in CPython › The problem reference counting cannot solve on its own: cycles (line 115) | may use names from earlier examples |
| `examples/05_the-problem-reference-counting-cannot-solve-on-i.py` | Reference counting in CPython › The problem reference counting cannot solve on its own: cycles (line 131) | may use names from earlier examples |
| `examples/06_weak-references-observe-without-owning.py` | Weak references observe without owning (line 182) | runs on its own |
| `examples/07_a-weak-set-can-still-have-strong-owners-elsewher.py` | Weak references observe without owning › A weak set can still have strong owners elsewhere (line 228) | runs on its own |
| `examples/08_support-for-weak-references-and-hashing-are-sepa.py` | Weak references observe without owning › Support for weak references and hashing are separate (line 272) | runs on its own |
| `examples/09_try-it-yourself.py` | Try it yourself (line 328) | runs on its own |
