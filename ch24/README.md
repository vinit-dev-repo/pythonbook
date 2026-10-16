# 24 - Custom Exceptions

The code of the chapter **24 - Custom Exceptions** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- The main branches of Python's built-in exception tree, and why normal handlers catch `Exception` instead of `BaseException`
- Why catching a type also catches every subclass of it
- Why and when to build your own exception classes
- How to add extra data to an exception, not just a message
- Building a small exception hierarchy for one module
- `raise ... from ...` — keeping (or hiding) the original cause of an error
- Following nested handlers and distinguishing stored diagnostic information from traceback display
- Repairing `Inventory` validation before it changes stock
- Building and assessing an `Account` with controlled overdraft and ledger snapshots

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `handler_names.py` | A handler name is deleted, not restored (line 260) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_catching-respects-inheritance.py` | Catching respects inheritance (line 109) | runs on its own |
| `examples/02_catching-respects-inheritance.py` | Catching respects inheritance (line 123) | may use names from earlier examples |
| `examples/03_why-make-your-own-exceptions.py` | Why make your own exceptions (line 147) | may use names from earlier examples |
| `examples/04_the-simplest-custom-exception.py` | The simplest custom exception (line 182) | raises an error on purpose |
| `examples/05_a-class-an-instance-and-its-message.py` | A class, an instance and its message (line 211) | may use names from earlier examples |
| `examples/06_a-class-an-instance-and-its-message.py` | A class, an instance and its message (line 236) | may use names from earlier examples |
| `examples/07_a-class-an-instance-and-its-message.py` | A class, an instance and its message (line 247) | may use names from earlier examples |
| `examples/08_adding-data-to-exceptions.py` | Adding data to exceptions (line 304) | may use names from earlier examples |
| `examples/09_transfer-check-both-ends-of-an-allowed-range.py` | Transfer: check both ends of an allowed range (line 337) | may use names from earlier examples |
| `examples/10_transfer-check-both-ends-of-an-allowed-range.py` | Transfer: check both ends of an allowed range (line 358) | may use names from earlier examples |
| `examples/11_give-the-handler-useful-behavior.py` | Give the handler useful behavior (line 391) | may use names from earlier examples |
| `examples/12_give-the-handler-useful-behavior.py` | Give the handler useful behavior (line 434) | may use names from earlier examples |
| `examples/13_choose-the-message-deliberately.py` | Choose the message deliberately (line 452) | may use names from earlier examples |
| `examples/14_choose-the-message-deliberately.py` | Choose the message deliberately (line 478) | may use names from earlier examples |
| `examples/15_choose-the-message-deliberately.py` | Choose the message deliberately (line 494) | may use names from earlier examples |
| `examples/16_building-a-small-hierarchy.py` | Building a small hierarchy (line 513) | may use names from earlier examples |
| `examples/17_building-a-small-hierarchy.py` | Building a small hierarchy (line 538) | may use names from earlier examples |
| `examples/18_choose-the-first-matching-handler.py` | Choose the first matching handler (line 573) | may use names from earlier examples |
| `examples/19_choose-the-first-matching-handler.py` | Choose the first matching handler (line 600) | may use names from earlier examples |
| `examples/20_keep-a-family-handler-stable.py` | Keep a family handler stable (line 620) | may use names from earlier examples |
| `examples/21_keep-a-family-handler-stable.py` | Keep a family handler stable (line 641) | may use names from earlier examples |
| `examples/22_follow-a-failure-through-nested-handlers.py` | Follow a failure through nested handlers (line 679) | may use names from earlier examples |
| `examples/23_raise-from-keeping-the-original-cause.py` | `raise ... from ...`: keeping the original cause (line 739) | raises an error on purpose |
| `examples/24_raise-from-keeping-the-original-cause.py` | `raise ... from ...`: keeping the original cause (line 779) | raises an error on purpose |
| `examples/25_stored-context-and-displayed-context-are-differe.py` | Stored context and displayed context are different (line 828) | may use names from earlier examples |
| `examples/26_stored-context-and-displayed-context-are-differe.py` | Stored context and displayed context are different (line 843) | may use names from earlier examples |
| `examples/27_a-chosen-cause-can-differ-from-the-current-conte.py` | A chosen cause can differ from the current context (line 860) | may use names from earlier examples |
| `examples/28_recovery-needs-a-clear-boundary.py` | Recovery needs a clear boundary (line 897) | may use names from earlier examples |
| `examples/29_recovery-needs-a-clear-boundary.py` | Recovery needs a clear boundary (line 914) | may use names from earlier examples |
| `examples/30_catching-does-not-undo-earlier-changes.py` | Catching does not undo earlier changes (line 939) | may use names from earlier examples |
| `examples/31_an-empty-result-can-be-valid.py` | An empty result can be valid (line 967) | may use names from earlier examples |
| `examples/32_an-empty-result-can-be-valid.py` | An empty result can be valid (line 986) | may use names from earlier examples |
| `examples/33_the-currently-handled-exception-can-change-tempo.py` | The currently handled exception can change temporarily (line 1014) | may use names from earlier examples |
| `examples/34_transfer-convert-a-value-without-hiding-the-wron.py` | Transfer: convert a value without hiding the wrong failure (line 1056) | may use names from earlier examples |
| `examples/35_transfer-convert-a-value-without-hiding-the-wron.py` | Transfer: convert a value without hiding the wrong failure (line 1125) | may use names from earlier examples |
| `examples/36_worked-example-a-tiny-inventory-module.py` | Worked example: a tiny inventory module (line 1163) | may use names from earlier examples |
| `examples/37_diagnose-an-invalid-request.py` | Diagnose an invalid request (line 1238) | may use names from earlier examples |
| `examples/38_validate-before-changing-stock.py` | Validate before changing stock (line 1270) | may use names from earlier examples |
| `examples/39_validate-before-changing-stock.py` | Validate before changing stock (line 1333) | may use names from earlier examples |
| `examples/40_account-identity-and-ledger-snapshots.py` | Account identity and ledger snapshots (line 1370) | may use names from earlier examples |
| `examples/41_overdraft-decisions-without-partial-state.py` | Overdraft decisions without partial state (line 1527) | may use names from earlier examples |
| `examples/42_trace-accepted-and-rejected-changes.py` | Trace accepted and rejected changes (line 1643) | may use names from earlier examples |
| `examples/43_a-saved-snapshot-keeps-its-old-length.py` | A saved snapshot keeps its old length (line 1707) | may use names from earlier examples |
| `examples/44_check-rejected-inputs-and-numeric-boundaries.py` | Check rejected inputs and numeric boundaries (line 1728) | may use names from earlier examples |
| `examples/45_build-and-explain-a-new-sequence.py` | Build and explain a new sequence (line 1806) | may use names from earlier examples |
| `examples/46_try-it-yourself.py` | Try it yourself (line 1862) | may use names from earlier examples |
