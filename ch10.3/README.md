# 10.3 - Raising, Asserting and Inspecting Exceptions

The code of the chapter **10.3 - Raising, Asserting and Inspecting Exceptions** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How to raise your own exceptions, and re-raise the same one
- `assert`, and why it can be switched off
- How to look at the current exception with `sys.exc_info()` and the `traceback` module

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `withdraw_bad.py` | `assert`: checking what you believe is true (line 110) |  |
| `withdraw_checked.py` | `assert`: checking what you believe is true (line 146) |  |
| `split_check.py` | `assert`: checking what you believe is true (line 174) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_raising-your-own-exceptions.py` | Raising your own exceptions (line 40) | raises an error on purpose |
| `examples/02_re-raising.py` | Raising your own exceptions › Re-raising (line 70) | raises an error on purpose |
| `examples/03_looking-at-the-exception-without-an-as-binding.py` | Looking at the exception without an `as` binding (line 223) | may use names from earlier examples |
| `examples/04_looking-at-the-exception-without-an-as-binding.py` | Looking at the exception without an `as` binding (line 247) | may use names from earlier examples |
| `examples/05_try-it-yourself.py` | Try it yourself (line 299) | may use names from earlier examples |
