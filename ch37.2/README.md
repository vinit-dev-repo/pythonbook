# 37.2 - Retained Objects, tracemalloc and Interning

The code of the chapter **37.2 - Retained Objects, tracemalloc and Interning** of the Python tutorial (folder `05 - Runtime`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Find caches and callbacks that keep objects in memory, then release and remeasure retained data.
- Use `tracemalloc` to locate traced allocations.
- Understand that integer caching and string interning are CPython details.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `retention_lab.py` | Objects kept in memory by mistake › Follow one retained allocation through release (line 162) |  |
| `test_retention_lab.py` | Objects kept in memory by mistake › Follow one retained allocation through release (line 242) |  |
| `exercise_retention.py` | Objects kept in memory by mistake › Practice: a second owner (line 301) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_leak-one-a-cache-that-never-forgets.py` | Objects kept in memory by mistake › Leak one: a cache that never forgets (line 44) | runs on its own |
| `examples/02_leak-one-a-cache-that-never-forgets.py` | Objects kept in memory by mistake › Leak one: a cache that never forgets (line 68) | may use names from earlier examples |
| `examples/03_leak-two-something-still-listening.py` | Objects kept in memory by mistake › Leak two: something still listening (line 93) | may use names from earlier examples |
| `examples/04_finding-a-leak-tracemalloc.py` | Objects kept in memory by mistake › Finding a leak: `tracemalloc` (line 130) | may use names from earlier examples |
| `examples/05_small-integers-are-pre-made.py` | Interning: reusing common objects › Small integers are pre-made (line 369) | may use names from earlier examples |
| `examples/06_small-integers-are-pre-made.py` | Interning: reusing common objects › Small integers are pre-made (line 381) | may use names from earlier examples |
| `examples/07_strings-get-a-similar-trick.py` | Interning: reusing common objects › Strings get a similar trick (line 398) | may use names from earlier examples |
| `examples/08_try-it-yourself.py` | Try it yourself (line 447) | runs on its own |
