# 33.2 - Building Iterators, Lazy Iterables, Built-ins and Delegation

The code of the chapter **33.2 - Building Iterators, Lazy Iterables, Built-ins and Delegation** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Build your own iterator class, and say why a separate iterable class matters.
- Say what a **lazy iterable** is and how it can save memory.
- Tour Python's built-in iterables and iterators, and read a file in blocks with `iter(callable, sentinel)`.
- Delegate `__iter__` to a wrapped collection.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `iterator_lifetime_lab.py` | Building your own iterator › Separating the collection from its iterator (line 105) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_every-iterator-is-also-an-iterable.py` | Every iterator is also an iterable (line 41) | runs on its own |
| `examples/02_building-your-own-iterator.py` | Building your own iterator (line 65) | may use names from earlier examples |
| `examples/03_a-cyclic-iterator.py` | Building your own iterator › A cyclic iterator (line 192) | may use names from earlier examples |
| `examples/04_lazy-iterables-values-made-on-demand.py` | Lazy iterables: values made on demand (line 238) | may use names from earlier examples |
| `examples/05_a-tour-of-python-s-built-in-iterables-and-iterat.py` | A tour of Python's built-in iterables and iterators (line 299) | may use names from earlier examples |
| `examples/06_iter-s-second-form-a-sentinel.py` | A tour of Python's built-in iterables and iterators › `iter()`'s second form: a sentinel (line 319) | may use names from earlier examples |
| `examples/07_delegating-iteration.py` | Delegating iteration (line 353) | may use names from earlier examples |
| `examples/08_try-it-yourself.py` | Try it yourself (line 399) | runs on its own |
