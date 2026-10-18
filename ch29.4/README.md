# 29.4 - Inheritance, Reusable Fields and Lazy Attributes

The code of the chapter **29.4 - Inheritance, Reusable Fields and Lazy Attributes** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- See how a descriptor is found through the MRO, and how a subclass can hide it.
- Build two reusable descriptors: a checked field and an attribute that computes once.
- Explain why a lazy cache needs a non-data descriptor, and how to make it compute again.

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_descriptors-and-inheritance-found-through-the-mr.py` | Descriptors and inheritance: found through the MRO (line 43) | runs on its own |
| `examples/02_a-subclass-can-shadow-the-descriptor-and-lose-th.py` | Descriptors and inheritance: found through the MRO › A subclass can shadow the descriptor and lose the protection (line 94) | may use names from earlier examples |
| `examples/03_application-1-a-reusable-validation-family.py` | Application 1: a reusable validation family (line 137) | may use names from earlier examples |
| `examples/04_continue-the-bounded-field-lab.py` | Application 1: a reusable validation family › Continue the bounded-field lab (line 237) | may use names from earlier examples |
| `examples/05_when-validation-also-changes-a-value.py` | Application 1: a reusable validation family › When validation also changes a value (line 261) | runs on its own |
| `examples/06_application-2-a-lazy-cached-attribute.py` | Application 2: a lazy (cached) attribute (line 328) | may use names from earlier examples |
| `examples/07_transfer-invalidate-a-lazy-cached-value.py` | Application 2: a lazy (cached) attribute › Transfer: invalidate a lazy cached value (line 382) | may use names from earlier examples |
| `examples/08_a-cache-that-does-not-cause-a-leak-weakvaluedict.py` | Application 2: a lazy (cached) attribute › A cache that does not cause a leak: `WeakValueDictionary` (line 403) | may use names from earlier examples |
| `examples/09_try-it-yourself.py` | Try it yourself (line 457) | runs on its own |
