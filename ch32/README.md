# 32 - The Sequence Protocol and Custom Sequences

The code of the chapter **32 - The Sequence Protocol and Custom Sequences** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What a **protocol** is and how Python uses supported operations
- How `__len__` and `__getitem__` provide the main sequence operations
- The difference between mutable and immutable sequences, and the extra methods mutable ones need
- What index `0` and a **half-open** slice mean
- How Python represents a slice with a `slice` object
- When `+=` changes an existing sequence and when it creates a new one
- How to build a sequence class step by step
- How `sorted()` and `.sort()` differ, including stable sorting

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `failed_sequence_store.py` | In-place concatenation and repetition › A failed store can leave a changed list (line 494) |  |
| `light_levels.py` | Put several protocols under one contract (line 896) |  |
| `counted_sequence_fragment.py` | List comprehensions, revisited › Extend the existing sequence and state what the counter means (line 1196) |  |
| `unique_sequence.py` | Keep first-seen order while removing duplicates (line 1261) |  |
| `list_invariant_fragment.py` | Keep first-seen order while removing duplicates › A constructor cannot protect every inherited list method (line 1356) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_the-sequence-protocol-len-and-getitem.py` | The sequence protocol: `__len__` and `__getitem__` (line 83) | runs on its own |
| `examples/02_mutable-vs-immutable-sequences.py` | Mutable vs immutable sequences (line 145) | may use names from earlier examples |
| `examples/03_mutable-vs-immutable-sequences.py` | Mutable vs immutable sequences (line 160) | raises an error on purpose |
| `examples/04_why-indexes-start-at-0-and-why-slices-are-half-o.py` | Why indexes start at 0, and why slices are half-open (line 207) | may use names from earlier examples |
| `examples/05_why-indexes-start-at-0-and-why-slices-are-half-o.py` | Why indexes start at 0, and why slices are half-open (line 231) | may use names from earlier examples |
| `examples/06_why-indexes-start-at-0-and-why-slices-are-half-o.py` | Why indexes start at 0, and why slices are half-open (line 250) | raises an error on purpose |
| `examples/07_copying-sequences-revisited.py` | Copying sequences, revisited (line 267) | may use names from earlier examples |
| `examples/08_copying-an-object-that-owns-a-sequence.py` | Copying sequences, revisited › Copying an object that owns a sequence (line 294) | runs on its own |
| `examples/09_slicing-in-depth-the-slice-object.py` | Slicing in depth: the slice object (line 336) | may use names from earlier examples |
| `examples/10_slicing-in-depth-the-slice-object.py` | Slicing in depth: the slice object (line 352) | may use names from earlier examples |
| `examples/11_supporting-slices-in-your-own-class.py` | Slicing in depth: the slice object › Supporting slices in your own class (line 366) | may use names from earlier examples |
| `examples/12_in-place-concatenation-and-repetition.py` | In-place concatenation and repetition (line 411) | may use names from earlier examples |
| `examples/13_in-place-concatenation-and-repetition.py` | In-place concatenation and repetition (line 428) | may use names from earlier examples |
| `examples/14_shared-lists-a-a-b-compared-with-a-b.py` | In-place concatenation and repetition › Shared lists: `a = a + b` compared with `a += b` (line 449) | may use names from earlier examples |
| `examples/15_shared-lists-a-a-b-compared-with-a-b.py` | In-place concatenation and repetition › Shared lists: `a = a + b` compared with `a += b` (line 466) | may use names from earlier examples |
| `examples/16_assignments-in-mutable-sequences.py` | Assignments in mutable sequences (line 539) | may use names from earlier examples |
| `examples/17_assignments-in-mutable-sequences.py` | Assignments in mutable sequences (line 552) | may use names from earlier examples |
| `examples/18_assignments-in-mutable-sequences.py` | Assignments in mutable sequences (line 565) | may use names from earlier examples |
| `examples/19_step-1-the-basic-protocol.py` | Worked project: building a full custom sequence › Step 1 — the basic protocol (line 595) | may use names from earlier examples |
| `examples/20_step-2-support-slices-too.py` | Worked project: building a full custom sequence › Step 2 — support slices too (line 640) | may use names from earlier examples |
| `examples/21_step-3-add-iadd-mul.py` | Worked project: building a full custom sequence › Step 3 — `__add__`, `__iadd__`, `__mul__` (line 685) | may use names from earlier examples |
| `examples/22_step-4-making-it-mutable.py` | Worked project: building a full custom sequence › Step 4 — making it mutable (line 757) | may use names from earlier examples |
| `examples/23_step-4-making-it-mutable.py` | Worked project: building a full custom sequence › Step 4 — making it mutable (line 854) | may use names from earlier examples |
| `examples/24_a-normalized-reverse-slice-is-a-range-of-indices.py` | Put several protocols under one contract › A normalized reverse slice is a range of indices (line 1012) | may use names from earlier examples |
| `examples/25_comparing-lists-and-tuples.py` | Comparing lists and tuples (line 1042) | may use names from earlier examples |
| `examples/26_sorting-sequences.py` | Sorting sequences (line 1083) | may use names from earlier examples |
| `examples/27_key-functions.py` | Sorting sequences › Key functions (line 1108) | may use names from earlier examples |
| `examples/28_stability-and-sorting-by-two-keys.py` | Sorting sequences › Stability, and sorting by two keys (line 1130) | may use names from earlier examples |
| `examples/29_list-comprehensions-revisited.py` | List comprehensions, revisited (line 1169) | may use names from earlier examples |
| `examples/30_try-it-yourself.py` | Try it yourself (line 1402) | may use names from earlier examples |
