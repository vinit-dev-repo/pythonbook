# 33.1 - Iterables, Iterators, the Protocol, the for Loop and Exhaustion

The code of the chapter **33.1 - Iterables, Iterators, the Protocol, the for Loop and Exhaustion** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- See how one protocol lets `for` work with lists, strings, files, dictionaries, and your own classes.
- Tell an **iterable** from an **iterator**.
- Say what a `for` loop *really* does, step by step.
- Say why an iterator is single-use and why some iterables support repeated loops.

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_the-problem-one-for-loop-many-different-things.py` | The problem: one `for` loop, many different things (line 42) | runs on its own |
| `examples/02_the-protocol-iter-next-and-stopiteration.py` | The protocol: `iter()`, `next()`, and `StopIteration` (line 108) | raises an error on purpose |
| `examples/03_what-a-for-loop-really-does.py` | What a `for` loop really does (line 142) | may use names from earlier examples |
| `examples/04_what-a-for-loop-really-does.py` | What a `for` loop really does (line 166) | may use names from earlier examples |
| `examples/05_iterators-are-single-use.py` | Iterators are single-use (line 206) | may use names from earlier examples |
| `examples/06_iterators-are-single-use.py` | Iterators are single-use (line 229) | may use names from earlier examples |
| `examples/07_try-it-yourself.py` | Try it yourself (line 280) | runs on its own |
