# 23.3 - Method Resolution Order, Mixins and Slots

The code of the chapter **23.3 - Method Resolution Order, Mixins and Slots** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- The Method Resolution Order (MRO): the order Python searches for a method
- How multiple inheritance, C3 and mixins shape that order
- How to find which class in a library owns a method
- `__slots__`: controlling instance storage in a compatible hierarchy

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `c3_order.py` | Method Resolution Order (MRO) › C3 preserves earlier ordering decisions (line 108) |  |
| `selected_method.py` | Method Resolution Order (MRO) › Select one method without reversing every lookup (line 157) |  |
| `inspect_frameworks.py` | Method Resolution Order (MRO) › Find the owner of a method in a library (line 254) |  |
| `slot_boundaries.py` | `__slots__`: a fixed attribute list › Slot names describe storage, not default values (line 427) |  |
| `measure_slots.py` | `__slots__`: a fixed attribute list › Measure a concrete slot workload (line 478) |  |
| `measure_slot_memory.py` | `__slots__`: a fixed attribute list › Measure retained allocations separately from time (line 536) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_method-resolution-order-mro.py` | Method Resolution Order (MRO) (line 40) | runs on its own |
| `examples/02_multiple-inheritance.py` | Method Resolution Order (MRO) › Multiple inheritance (line 65) | may use names from earlier examples |
| `examples/03_reusing-a-narrow-behavior-with-a-mixin.py` | Method Resolution Order (MRO) › Reusing a narrow behavior with a mixin (line 211) | may use names from earlier examples |
| `examples/04_slots-a-fixed-attribute-list.py` | `__slots__`: a fixed attribute list (line 330) | raises an error on purpose |
| `examples/05_slots-and-dictionaries-across-a-hierarchy.py` | `__slots__`: a fixed attribute list › Slots and dictionaries across a hierarchy (line 364) | may use names from earlier examples |
| `examples/06_try-it-yourself.py` | Try it yourself (line 623) | may use names from earlier examples |
