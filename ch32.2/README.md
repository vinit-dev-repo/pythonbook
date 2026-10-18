# 32.2 - Indexes, Slices, Copies, In-Place Operators and Slice Assignment

The code of the chapter **32.2 - Indexes, Slices, Copies, In-Place Operators and Slice Assignment** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Explain why indexes start at `0` and what a **half-open** slice means.
- Tell a shallow copy from a deep copy, for a list and for an object that owns a list.
- Say how Python represents a slice with a `slice` object, and make your own class accept slices.
- Say when `+=` changes an existing sequence and when it creates a new one.
- Replace and delete ranges with slice assignment.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `failed_sequence_store.py` | In-place concatenation and repetition › A failed store can leave a changed list (line 329) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_why-indexes-start-at-0-and-why-slices-are-half-o.py` | Why indexes start at 0, and why slices are half-open (line 54) | runs on its own |
| `examples/02_why-indexes-start-at-0-and-why-slices-are-half-o.py` | Why indexes start at 0, and why slices are half-open (line 78) | may use names from earlier examples |
| `examples/03_why-indexes-start-at-0-and-why-slices-are-half-o.py` | Why indexes start at 0, and why slices are half-open (line 97) | raises an error on purpose |
| `examples/04_copying-sequences-revisited.py` | Copying sequences, revisited (line 116) | may use names from earlier examples |
| `examples/05_copying-an-object-that-owns-a-sequence.py` | Copying sequences, revisited › Copying an object that owns a sequence (line 140) | runs on its own |
| `examples/06_slicing-in-depth-the-slice-object.py` | Slicing in depth: the slice object (line 183) | may use names from earlier examples |
| `examples/07_slicing-in-depth-the-slice-object.py` | Slicing in depth: the slice object (line 198) | may use names from earlier examples |
| `examples/08_supporting-slices-in-your-own-class.py` | Slicing in depth: the slice object › Supporting slices in your own class (line 210) | may use names from earlier examples |
| `examples/09_in-place-concatenation-and-repetition.py` | In-place concatenation and repetition (line 254) | may use names from earlier examples |
| `examples/10_in-place-concatenation-and-repetition.py` | In-place concatenation and repetition (line 270) | may use names from earlier examples |
| `examples/11_shared-lists-a-a-b-compared-with-a-b.py` | In-place concatenation and repetition › Shared lists: `a = a + b` compared with `a += b` (line 289) | may use names from earlier examples |
| `examples/12_shared-lists-a-a-b-compared-with-a-b.py` | In-place concatenation and repetition › Shared lists: `a = a + b` compared with `a += b` (line 305) | may use names from earlier examples |
| `examples/13_assignments-in-mutable-sequences.py` | Assignments in mutable sequences (line 375) | may use names from earlier examples |
| `examples/14_assignments-in-mutable-sequences.py` | Assignments in mutable sequences (line 387) | may use names from earlier examples |
| `examples/15_assignments-in-mutable-sequences.py` | Assignments in mutable sequences (line 399) | may use names from earlier examples |
| `examples/16_try-it-yourself.py` | Try it yourself (line 444) | runs on its own |
