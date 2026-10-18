# 31a - Project - Validated Fields - Preserve Behavior While Refactoring

The code of the chapter **31a - Project - Validated Fields - Preserve Behavior While Refactoring** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## About this chapter

A reusable field needs more than a valid-value example. Its callers also rely on omitted arguments, error behavior and independent instance storage. In this project, build those rules first, test them, then move repeated mechanics into a base class without changing what callers observe.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

The chapter saves these files more than once (for example a first version and a repaired one). This folder holds the version the chapter ends with, and the table points to that last version:

- `fields.py`

| File | Where it is in the chapter | Note |
|---|---|---|
| `field_demo.py` | Session 1: independent fields, bounds, and storage (line 142) |  |
| `test_fields.py` | Session 1: independent fields, bounds, and storage (line 184) |  |
| `binding_demo.py` | Session 2: class creation and late attachment (line 366) |  |
| `fields.py` | Session 3: refactor without losing constructors (line 446) | rewritten later in the chapter |
| `base_demo.py` | Session 3: refactor without losing constructors › Check the base contract (line 540) |  |
| `assignment_demo.py` | Session 3: refactor without losing constructors › Check the base contract (line 578) |  |
| `booking_transfer.py` | Transfer: Booking fields (line 646) |  |
