# 27.4 - Shared State, Caches and Registration

The code of the chapter **27.4 - Shared State, Caches and Registration** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Diagnose accidental shared state and distinguish it from deliberate caching and registration.
- Repair a shared wrapper by returning a new wrapper for each construction.
- Keep the first instance as a stated policy, and see that later arguments are ignored.
- Register an object and return it unchanged, and choose development-only decoration explicitly.
- Predict a third construction by finding the object that owns the state.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `development_decoration.py` | Choose development-only decoration explicitly (line 270) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_a-shared-wrapper-can-silently-overwrite-an-earli.py` | A shared wrapper can silently overwrite an earlier record (line 45) | runs on its own |
| `examples/02_a-shared-wrapper-can-silently-overwrite-an-earli.py` | A shared wrapper can silently overwrite an earlier record (line 89) | runs on its own |
| `examples/03_deliberate-first-instance-caching.py` | Deliberate first-instance caching (line 137) | runs on its own |
| `examples/04_registration-can-leave-later-calls-unchanged.py` | Registration can leave later calls unchanged (line 197) | runs on its own |
| `examples/05_try-it-yourself.py` | Try it yourself (line 361) | runs on its own |
