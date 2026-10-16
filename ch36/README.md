# 36 - Context Managers

The code of the chapter **36 - Context Managers** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why a program must release resources after success or failure
- How `try`/`finally` guarantees cleanup
- How the `with` statement manages setup and cleanup
- How `with` calls `__enter__` and `__exit__`, and how it relates to `try`/`finally`
- How to write your own context manager class
- What the three `__exit__` arguments mean and how its return value controls an exception
- That context managers are not only for cleanup — they can also switch a "mode" on and off
- How `@contextlib.contextmanager` turns a generator into a context manager
- A tour of `contextlib`'s ready-made helpers, and how to nest several context managers at once

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `managed_csv_records.py` | Transfer project: own a lazy CSV stream until its last use (line 994) |  |
| `aligned_records.py` | Transfer project: combine four aligned record streams (line 1282) |  |
| `site_report.py` | Transfer project: combine four aligned record streams (line 1386) |  |
| `group_lifetime_lab.py` | Transfer project: combine four aligned record streams › Diagnose an exhausted mask and shared groups (line 1487) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_try-finally-the-manual-way.py` | `try`/`finally`: the manual way (line 67) | raises an error on purpose |
| `examples/02_with-the-same-guarantee-packaged.py` | `with`: the same guarantee, packaged (line 99) | may use names from earlier examples |
| `examples/03_what-with-really-does.py` | What `with` really does (line 128) | may use names from earlier examples |
| `examples/04_writing-your-own-context-manager-class.py` | Writing your own context manager class (line 190) | may use names from earlier examples |
| `examples/05_writing-your-own-context-manager-class.py` | Writing your own context manager class (line 207) | may use names from earlier examples |
| `examples/06_writing-your-own-context-manager-class.py` | Writing your own context manager class (line 229) | may use names from earlier examples |
| `examples/07_writing-your-own-context-manager-class.py` | Writing your own context manager class (line 258) | may use names from earlier examples |
| `examples/08_exit-s-three-arguments.py` | `__exit__`'s three arguments (line 294) | raises an error on purpose |
| `examples/09_swallowing-exceptions-exit-s-return-value.py` | Swallowing exceptions: `__exit__`'s return value (line 344) | may use names from earlier examples |
| `examples/10_swallowing-exceptions-exit-s-return-value.py` | Swallowing exceptions: `__exit__`'s return value (line 372) | raises an error on purpose |
| `examples/11_context-managers-are-not-only-for-cleanup.py` | Context managers are not only for cleanup (line 411) | may use names from earlier examples |
| `examples/12_context-managers-are-not-only-for-cleanup.py` | Context managers are not only for cleanup (line 428) | may use names from earlier examples |
| `examples/13_context-managers-are-not-only-for-cleanup.py` | Context managers are not only for cleanup (line 445) | may use names from earlier examples |
| `examples/14_lazy-iterators-from-closed-resources.py` | Lazy iterators from closed resources (line 480) | raises an error on purpose |
| `examples/15_lazy-iterators-from-closed-resources.py` | Lazy iterators from closed resources (line 502) | may use names from earlier examples |
| `examples/16_generators-context-managers.py` | Generators + context managers (line 530) | may use names from earlier examples |
| `examples/17_generators-context-managers.py` | Generators + context managers (line 543) | may use names from earlier examples |
| `examples/18_generators-context-managers.py` | Generators + context managers (line 559) | may use names from earlier examples |
| `examples/19_generators-context-managers.py` | Generators + context managers (line 579) | may use names from earlier examples |
| `examples/20_a-tour-of-contextlib.py` | A tour of `contextlib` (line 616) | may use names from earlier examples |
| `examples/21_a-tour-of-contextlib.py` | A tour of `contextlib` (line 631) | may use names from earlier examples |
| `examples/22_a-tour-of-contextlib.py` | A tour of `contextlib` (line 655) | may use names from earlier examples |
| `examples/23_nesting-context-managers.py` | Nesting context managers (line 683) | may use names from earlier examples |
| `examples/24_nesting-context-managers.py` | Nesting context managers (line 702) | may use names from earlier examples |
| `examples/25_nesting-context-managers.py` | Nesting context managers (line 718) | may use names from earlier examples |
| `examples/26_observe-failed-entry-binding-and-cleanup.py` | Observe failed entry, binding and cleanup (line 757) | may use names from earlier examples |
| `examples/27_an-exception-travels-back-to-yield.py` | An exception travels back to `yield` (line 836) | may use names from earlier examples |
| `examples/28_an-exception-travels-back-to-yield.py` | An exception travels back to `yield` (line 893) | may use names from earlier examples |
| `examples/29_dynamic-resources-the-second-open-fails.py` | Dynamic resources: the second open fails (line 927) | may use names from earlier examples |
| `examples/30_try-it-yourself.py` | Try it yourself (line 1584) | may use names from earlier examples |
