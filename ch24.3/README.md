# 24.3 - Nested Handlers, Causes and Recovery

The code of the chapter **24.3 - Nested Handlers, Causes and Recovery** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Following nested handlers and distinguishing stored diagnostic information from traceback display
- `raise ... from ...`: keeping (or hiding) the original cause of an error
- Why a handler needs a clear boundary, and what catching does not undo
- A converter with a deliberate failure policy, and good practices for custom exceptions

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_follow-a-failure-through-nested-handlers.py` | Follow a failure through nested handlers (line 54) | runs on its own |
| `examples/02_raise-from-keeping-the-original-cause.py` | `raise ... from ...`: keeping the original cause (line 117) | raises an error on purpose |
| `examples/03_raise-from-keeping-the-original-cause.py` | `raise ... from ...`: keeping the original cause (line 160) | raises an error on purpose |
| `examples/04_stored-context-and-displayed-context-are-differe.py` | `raise ... from ...`: keeping the original cause › Stored context and displayed context are different (line 208) | may use names from earlier examples |
| `examples/05_stored-context-and-displayed-context-are-differe.py` | `raise ... from ...`: keeping the original cause › Stored context and displayed context are different (line 226) | may use names from earlier examples |
| `examples/06_a-chosen-cause-can-differ-from-the-current-conte.py` | `raise ... from ...`: keeping the original cause › A chosen cause can differ from the current context (line 241) | may use names from earlier examples |
| `examples/07_recovery-needs-a-clear-boundary.py` | Recovery needs a clear boundary (line 281) | may use names from earlier examples |
| `examples/08_recovery-needs-a-clear-boundary.py` | Recovery needs a clear boundary (line 297) | may use names from earlier examples |
| `examples/09_catching-does-not-undo-earlier-changes.py` | Recovery needs a clear boundary › Catching does not undo earlier changes (line 320) | may use names from earlier examples |
| `examples/10_an-empty-result-can-be-valid.py` | Recovery needs a clear boundary › An empty result can be valid (line 347) | may use names from earlier examples |
| `examples/11_an-empty-result-can-be-valid.py` | Recovery needs a clear boundary › An empty result can be valid (line 365) | may use names from earlier examples |
| `examples/12_the-currently-handled-exception-can-change-tempo.py` | Recovery needs a clear boundary › The currently handled exception can change temporarily (line 391) | may use names from earlier examples |
| `examples/13_transfer-convert-a-value-without-hiding-the-wron.py` | Transfer: convert a value without hiding the wrong failure (line 436) | may use names from earlier examples |
| `examples/14_transfer-convert-a-value-without-hiding-the-wron.py` | Transfer: convert a value without hiding the wrong failure (line 504) | may use names from earlier examples |
| `examples/15_try-it-yourself.py` | Try it yourself (line 563) | may use names from earlier examples |
