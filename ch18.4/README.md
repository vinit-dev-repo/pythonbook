# 18.4 - Dispatching and Common Uses

The code of the chapter **18.4 - Dispatching and Common Uses** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How to make one function behave differently depending on the *type* of its argument (dispatching)
- How an exact-type registry and `functools.singledispatch` choose differently for `True`
- Which common job each decorator of the chapter does

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_the-naive-way-a-chain-of-isinstance-checks.py` | Dispatching: different behaviour by type › The naive way: a chain of `isinstance` checks (line 43) | runs on its own |
| `examples/02_a-hand-rolled-registry.py` | Dispatching: different behaviour by type › A hand-rolled registry (line 60) | may use names from earlier examples |
| `examples/03_a-hand-rolled-registry.py` | Dispatching: different behaviour by type › A hand-rolled registry (line 94) | may use names from earlier examples |
| `examples/04_functools-singledispatch-the-built-in-version.py` | Dispatching: different behaviour by type › `functools.singledispatch`: the built-in version (line 112) | may use names from earlier examples |
| `examples/05_functools-singledispatch-the-built-in-version.py` | Dispatching: different behaviour by type › `functools.singledispatch`: the built-in version (line 152) | may use names from earlier examples |
| `examples/06_try-it-yourself.py` | Try it yourself (line 217) | may use names from earlier examples |
