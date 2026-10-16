# 33 - Iterables and Iterators

The code of the chapter **33 - Iterables and Iterators** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How one protocol lets `for` work with lists, strings, files, dictionaries, and your own classes
- The difference between an **iterable** and an **iterator**
- What a `for` loop *really* does, step by step
- Why an iterator is single-use and why some iterables support repeated loops
- How to build your own iterator class, and why a separate iterable class matters
- What a **lazy iterable** is and how it can save memory
- A tour of Python's built-in iterables and iterators
- What happens when two functions consume the same iterator

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `iterator_lifetime_lab.py` | Building your own iterator › Separating the collection from its iterator (line 329) |  |
| `membership_paths.py` | Membership chooses its own method (line 727) |  |
| `polygon_catalogue.py` | Transfer project: a polygon catalogue that changes its storage strategy (line 826) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_the-problem-one-for-loop-many-different-things.py` | The problem: one `for` loop, many different things (line 47) | runs on its own |
| `examples/02_the-protocol-iter-next-and-stopiteration.py` | The protocol: `iter()`, `next()`, and `StopIteration` (line 110) | raises an error on purpose |
| `examples/03_what-a-for-loop-really-does.py` | What a `for` loop really does (line 142) | may use names from earlier examples |
| `examples/04_what-a-for-loop-really-does.py` | What a `for` loop really does (line 167) | may use names from earlier examples |
| `examples/05_iterators-are-single-use.py` | Iterators are single-use (line 205) | may use names from earlier examples |
| `examples/06_iterators-are-single-use.py` | Iterators are single-use (line 229) | may use names from earlier examples |
| `examples/07_every-iterator-is-also-an-iterable.py` | Every iterator is also an iterable (line 264) | may use names from earlier examples |
| `examples/08_building-your-own-iterator.py` | Building your own iterator (line 287) | may use names from earlier examples |
| `examples/09_a-cyclic-iterator.py` | Building your own iterator › A cyclic iterator (line 419) | may use names from earlier examples |
| `examples/10_lazy-iterables-values-made-on-demand.py` | Lazy iterables: values made on demand (line 463) | may use names from earlier examples |
| `examples/11_a-tour-of-python-s-built-in-iterables-and-iterat.py` | A tour of Python's built-in iterables and iterators (line 522) | may use names from earlier examples |
| `examples/12_iter-s-second-form-a-sentinel.py` | A tour of Python's built-in iterables and iterators › `iter()`'s second form: a sentinel (line 544) | may use names from earlier examples |
| `examples/13_delegating-iteration.py` | Delegating iteration (line 578) | may use names from earlier examples |
| `examples/14_reversed-iteration.py` | Reversed iteration (line 608) | may use names from earlier examples |
| `examples/15_an-iterator-is-single-use.py` | An iterator is single-use (line 647) | raises an error on purpose |
| `examples/16_an-iterator-is-single-use.py` | An iterator is single-use (line 670) | may use names from earlier examples |
| `examples/17_sorting-any-iterable.py` | Sorting any iterable (line 692) | may use names from earlier examples |
| `examples/18_try-it-yourself.py` | Try it yourself (line 1146) | may use names from earlier examples |
