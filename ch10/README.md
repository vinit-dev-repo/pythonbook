# 10 - Errors and Exceptions

The code of the chapter **10 - Errors and Exceptions** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- The three different ways a program can go wrong, and how to tell them apart
- What an exception is, how a handler can respond, and when an unhandled exception ends a script
- How to read a traceback from the bottom up, so error messages stop feeling scary
- The exception types you will meet almost every day, and what triggers each one
- How to catch errors with `try`/`except`, and why a bare `except:` is dangerous
- `else` and `finally` — the two less-famous parts of error handling
- How to raise your own exceptions, and when you should just let one crash the program

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `read_change.py` | Convert user input at a narrow boundary (line 542) |  |
| `withdraw_bad.py` | `assert`: checking what you believe is true (line 675) |  |
| `withdraw_checked.py` | `assert`: checking what you believe is true (line 712) |  |
| `split_check.py` | `assert`: checking what you believe is true (line 741) |  |
| `ask_age.py` | When to catch an exception (line 903) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_three-ways-a-program-can-go-wrong.py` | Three ways a program can go wrong (line 52) | raises an error on purpose |
| `examples/02_three-ways-a-program-can-go-wrong.py` | Three ways a program can go wrong (line 67) | raises an error on purpose |
| `examples/03_three-ways-a-program-can-go-wrong.py` | Three ways a program can go wrong (line 87) | may use names from earlier examples |
| `examples/04_what-an-exception-really-is.py` | What an exception really is (line 122) | raises an error on purpose |
| `examples/05_reading-a-traceback-from-the-last-line.py` | Reading a traceback from the last line (line 159) | raises an error on purpose |
| `examples/06_the-common-exception-types.py` | The common exception types (line 218) | raises an error on purpose |
| `examples/07_the-common-exception-types.py` | The common exception types (line 232) | raises an error on purpose |
| `examples/08_the-common-exception-types.py` | The common exception types (line 246) | raises an error on purpose |
| `examples/09_the-common-exception-types.py` | The common exception types (line 260) | raises an error on purpose |
| `examples/10_the-common-exception-types.py` | The common exception types (line 275) | raises an error on purpose |
| `examples/11_the-common-exception-types.py` | The common exception types (line 290) | raises an error on purpose |
| `examples/12_the-common-exception-types.py` | The common exception types (line 304) | raises an error on purpose |
| `examples/13_when-the-message-suggests-a-fix.py` | The common exception types › When the message suggests a fix (line 329) | raises an error on purpose |
| `examples/14_when-the-message-suggests-a-fix.py` | The common exception types › When the message suggests a fix (line 346) | raises an error on purpose |
| `examples/15_catching-exceptions-try-except.py` | Catching exceptions: try/except (line 368) | may use names from earlier examples |
| `examples/16_catch-a-specific-type-never-a-bare-except.py` | Catching exceptions: try/except › Catch a specific type — never a bare `except` (line 394) | may use names from earlier examples |
| `examples/17_catching-several-types.py` | Catching exceptions: try/except › Catching several types (line 418) | may use names from earlier examples |
| `examples/18_catching-several-types.py` | Catching exceptions: try/except › Catching several types (line 440) | may use names from earlier examples |
| `examples/19_getting-the-exception-object-with-as.py` | Catching exceptions: try/except › Getting the exception object with `as` (line 471) | may use names from earlier examples |
| `examples/20_else-and-finally.py` | `else` and `finally` (line 502) | may use names from earlier examples |
| `examples/21_convert-user-input-at-a-narrow-boundary.py` | Convert user input at a narrow boundary (line 572) | may use names from earlier examples |
| `examples/22_raising-your-own-exceptions.py` | Raising your own exceptions (line 607) | raises an error on purpose |
| `examples/23_re-raising.py` | Raising your own exceptions › Re-raising (line 638) | raises an error on purpose |
| `examples/24_looking-at-the-exception-without-an-as-binding.py` | Looking at the exception without an `as` binding (line 788) | may use names from earlier examples |
| `examples/25_looking-at-the-exception-without-an-as-binding.py` | Looking at the exception without an `as` binding (line 812) | may use names from earlier examples |
| `examples/26_breaking-out-of-nested-loops-with-an-exception.py` | Breaking out of nested loops with an exception (line 851) | may use names from earlier examples |
| `examples/27_when-to-catch-an-exception.py` | When to catch an exception (line 893) | may use names from earlier examples |
| `examples/28_eafp-vs-lbyl.py` | EAFP vs LBYL (line 946) | may use names from earlier examples |
| `examples/29_try-it-yourself.py` | Try it yourself (line 1002) | may use names from earlier examples |
