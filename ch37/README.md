# 37 - Object Lifetime and Memory Management

The code of the chapter **37 - Object Lifetime and Memory Management** of the Python tutorial (folder `05 - Runtime`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Explain CPython reference counts and unreachable reference cycles.
- Find caches and callbacks that keep objects in memory, then release and remeasure retained data.
- Use `tracemalloc` to locate traced allocations.
- Understand that integer caching and string interning are CPython details.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `retention_lab.py` | Objects kept in memory by mistake › Follow one retained allocation through release (line 444) |  |
| `test_retention_lab.py` | Objects kept in memory by mistake › Follow one retained allocation through release (line 531) |  |
| `exercise_retention.py` | Objects kept in memory by mistake › Practice: a second owner (line 593) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_reference-counting-in-cpython.py` | Reference counting in CPython (line 50) | runs on its own |
| `examples/02_reference-counting-in-cpython.py` | Reference counting in CPython (line 64) | may use names from earlier examples |
| `examples/03_when-the-count-hits-zero.py` | Reference counting in CPython › When the count hits zero (line 83) | may use names from earlier examples |
| `examples/04_the-problem-reference-counting-cannot-solve-on-i.py` | Reference counting in CPython › The problem reference counting cannot solve on its own: cycles (line 122) | may use names from earlier examples |
| `examples/05_the-problem-reference-counting-cannot-solve-on-i.py` | Reference counting in CPython › The problem reference counting cannot solve on its own: cycles (line 139) | may use names from earlier examples |
| `examples/06_weak-references-observe-without-owning.py` | Weak references observe without owning (line 187) | runs on its own |
| `examples/07_a-weak-set-can-still-have-strong-owners-elsewher.py` | Weak references observe without owning › A weak set can still have strong owners elsewhere (line 233) | runs on its own |
| `examples/08_support-for-weak-references-and-hashing-are-sepa.py` | Weak references observe without owning › Support for weak references and hashing are separate (line 279) | runs on its own |
| `examples/09_leak-one-a-cache-that-never-forgets.py` | Objects kept in memory by mistake › Leak one: a cache that never forgets (line 321) | may use names from earlier examples |
| `examples/10_leak-one-a-cache-that-never-forgets.py` | Objects kept in memory by mistake › Leak one: a cache that never forgets (line 344) | may use names from earlier examples |
| `examples/11_leak-two-something-still-listening.py` | Objects kept in memory by mistake › Leak two: something still listening (line 372) | may use names from earlier examples |
| `examples/12_finding-a-leak-tracemalloc.py` | Objects kept in memory by mistake › Finding a leak: `tracemalloc` (line 412) | may use names from earlier examples |
| `examples/13_small-integers-are-pre-made.py` | Interning: reusing common objects › Small integers are pre-made (line 658) | may use names from earlier examples |
| `examples/14_small-integers-are-pre-made.py` | Interning: reusing common objects › Small integers are pre-made (line 671) | may use names from earlier examples |
| `examples/15_strings-get-a-similar-trick.py` | Interning: reusing common objects › Strings get a similar trick (line 690) | may use names from earlier examples |
| `examples/16_try-it-yourself.py` | Try it yourself (line 737) | may use names from earlier examples |
