# 26.2 - collections.abc and Writing Your Own ABC

The code of the chapter **26.2 - collections.abc and Writing Your Own ABC** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- The main `collections.abc` classes and the dunder methods each one requires
- Why recognition by an ABC is not the same as a working operation
- How the `numbers` tower works, and its limits for `bool` and `Decimal`
- How to write your own abstract base class with `abc.ABC` and `@abstractmethod`
- How an abstract method can have a body, and where `@abstractmethod` goes under another decorator

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_standard-interfaces-in-collections-abc.py` | Standard interfaces in `collections.abc` (line 44) | runs on its own |
| `examples/02_standard-interfaces-in-collections-abc.py` | Standard interfaces in `collections.abc` (line 92) | runs on its own |
| `examples/03_standard-interfaces-in-collections-abc.py` | Standard interfaces in `collections.abc` (line 127) | runs on its own |
| `examples/04_numeric-contracts-the-numbers-abc-tower.py` | Standard interfaces in `collections.abc` › Numeric contracts: the `numbers` ABC tower (line 167) | runs on its own |
| `examples/05_writing-your-own-abc.py` | Writing your own ABC (line 208) | runs on its own |
| `examples/06_an-abstract-method-can-sit-beside-a-working-one.py` | Writing your own ABC › An abstract method can sit beside a working one (line 244) | runs on its own |
| `examples/07_an-abstract-method-can-sit-beside-a-working-one.py` | Writing your own ABC › An abstract method can sit beside a working one (line 302) | runs on its own |
| `examples/08_an-abstract-method-can-sit-beside-a-working-one.py` | Writing your own ABC › An abstract method can sit beside a working one (line 337) | runs on its own |
| `examples/09_an-abstract-method-can-sit-beside-a-working-one.py` | Writing your own ABC › An abstract method can sit beside a working one (line 382) | runs on its own |
| `examples/10_try-it-yourself.py` | Try it yourself (line 478) | runs on its own |
