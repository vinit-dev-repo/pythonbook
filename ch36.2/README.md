# 36.2 - Exit Arguments, Suppressing Errors, Temporary State, Lazy Iterators and Generator Managers

The code of the chapter **36.2 - Exit Arguments, Suppressing Errors, Temporary State, Lazy Iterators and Generator Managers** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What the three `__exit__` arguments mean and how its return value controls an exception
- That context managers are not only for cleanup: they can also switch a "mode" on and off
- Why a lazy iterator over a closed resource fails, and how to avoid that
- How `@contextlib.contextmanager` turns a generator into a context manager

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_exit-s-three-arguments.py` | `__exit__`'s three arguments (line 51) | raises an error on purpose |
| `examples/02_swallowing-exceptions-exit-s-return-value.py` | Swallowing exceptions: `__exit__`'s return value (line 102) | may use names from earlier examples |
| `examples/03_swallowing-exceptions-exit-s-return-value.py` | Swallowing exceptions: `__exit__`'s return value (line 130) | raises an error on purpose |
| `examples/04_context-managers-are-not-only-for-cleanup.py` | Context managers are not only for cleanup (line 171) | may use names from earlier examples |
| `examples/05_context-managers-are-not-only-for-cleanup.py` | Context managers are not only for cleanup (line 188) | may use names from earlier examples |
| `examples/06_context-managers-are-not-only-for-cleanup.py` | Context managers are not only for cleanup (line 205) | may use names from earlier examples |
| `examples/07_lazy-iterators-from-closed-resources.py` | Lazy iterators from closed resources (line 242) | raises an error on purpose |
| `examples/08_lazy-iterators-from-closed-resources.py` | Lazy iterators from closed resources (line 263) | may use names from earlier examples |
| `examples/09_generators-context-managers.py` | Generators + context managers (line 293) | may use names from earlier examples |
| `examples/10_generators-context-managers.py` | Generators + context managers (line 306) | may use names from earlier examples |
| `examples/11_generators-context-managers.py` | Generators + context managers (line 322) | may use names from earlier examples |
| `examples/12_generators-context-managers.py` | Generators + context managers (line 341) | may use names from earlier examples |
| `examples/13_try-it-yourself.py` | Try it yourself (line 387) | runs on its own |
