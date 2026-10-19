# 33.3 - Reversed Iteration, Consumed Iterators, Sorting and Membership

The code of the chapter **33.3 - Reversed Iteration, Consumed Iterators, Sorting and Membership** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Use `reversed()`, and add `__reversed__` to your own class.
- Say what happens when two functions consume the same iterator.
- Sort any finite iterable with `sorted()`.
- Say which method `in` uses: `__contains__`, iteration or the index fallback.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `membership_paths.py` | Membership chooses its own method (line 165) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_reversed-iteration.py` | Reversed iteration (line 41) | runs on its own |
| `examples/02_an-iterator-is-single-use.py` | An iterator is single-use (line 83) | raises an error on purpose |
| `examples/03_an-iterator-is-single-use.py` | An iterator is single-use (line 104) | may use names from earlier examples |
| `examples/04_sorting-any-iterable.py` | Sorting any iterable (line 128) | may use names from earlier examples |
| `examples/05_try-it-yourself.py` | Try it yourself (line 253) | runs on its own |
