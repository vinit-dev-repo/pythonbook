# 26.3 - Virtual Subclasses and Subclass Hooks

The code of the chapter **26.3 - Virtual Subclasses and Subclass Hooks** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How `.register()` makes a virtual subclass without adding inheritance
- What registration changes (`isinstance`, `issubclass`) and what it leaves alone (the MRO, inherited code)
- How an adapter supplies a shared helper that a registered class lacks
- How `__subclasshook__` lets an ABC recognize a class with no registration
- How real inheritance, registration and a hook differ in one table

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_virtual-subclasses-register.py` | Virtual subclasses: `.register()` (line 44) | runs on its own |
| `examples/02_virtual-subclasses-register.py` | Virtual subclasses: `.register()` (line 94) | runs on its own |
| `examples/03_virtual-subclasses-register.py` | Virtual subclasses: `.register()` (line 144) | runs on its own |
| `examples/04_virtual-subclasses-register.py` | Virtual subclasses: `.register()` (line 178) | runs on its own |
| `examples/05_virtual-subclasses-register.py` | Virtual subclasses: `.register()` (line 221) | runs on its own |
| `examples/06_subclasshook-isinstance-with-no-registration-eit.py` | `__subclasshook__`: `isinstance` with no registration either (line 259) | runs on its own |
| `examples/07_subclasshook-isinstance-with-no-registration-eit.py` | `__subclasshook__`: `isinstance` with no registration either (line 286) | runs on its own |
| `examples/08_try-it-yourself.py` | Try it yourself (line 375) | runs on its own |
