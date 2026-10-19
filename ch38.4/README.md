# 38.4 - Cached Bytecode, exec and eval, Future Imports, Implementations and Constant Folding

The code of the chapter **38.4 - Cached Bytecode, exec and eval, Future Imports, Implementations and Constant Folding** of the Python tutorial (folder `05 - Runtime`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What a `.pyc` file caches, and what it does NOT cache
- Why `eval()` and `exec()` need trusted input
- What a `__future__` import and constant folding change at compile time
- Why CPython is one implementation, not the language

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `step1_first_import.py` | `.pyc` files and `__pycache__` (line 62) |  |
| `step3_edit_and_reimport.py` | `.pyc` files and `__pycache__` (line 97) |  |
| `sourceless_cache.py` | `.pyc` files and `__pycache__` › A cached file without its source (line 144) |  |
| `cache_validation_modes.py` | `.pyc` files and `__pycache__` › Timestamp checks and checked-hash caches (line 194) |  |
| `source_file_namespace.py` | `exec()` and `eval()`: running code you build at runtime › Executing a trusted source file in a chosen namespace (line 362) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_pyc-files-and-pycache.py` | `.pyc` files and `__pycache__` (line 43) | runs on its own |
| `examples/02_pyc-files-and-pycache.py` | `.pyc` files and `__pycache__` (line 80) | runs on its own |
| `examples/03_a-class-body-also-has-compiled-code.py` | `.pyc` files and `__pycache__` › A class body also has compiled code (line 243) | runs on its own |
| `examples/04_exec-and-eval-running-code-you-build-at-runtime.py` | `exec()` and `eval()`: running code you build at runtime (line 300) | may use names from earlier examples |
| `examples/05_exec-and-eval-running-code-you-build-at-runtime.py` | `exec()` and `eval()`: running code you build at runtime (line 332) | raises an error on purpose |
| `examples/06_future-opting-in-to-a-change-early.py` | `__future__`: opting in to a change early (line 410) | runs on its own |
| `examples/07_future-opting-in-to-a-change-early.py` | `__future__`: opting in to a change early (line 415) | may use names from earlier examples |
| `examples/08_constant-folding.py` | Compile-time optimisations: constant folding › Constant folding (line 514) | runs on its own |
| `examples/09_small-literal-sequences-get-folded-too-large-one.py` | Compile-time optimisations: constant folding › Small literal sequences get folded too: large ones don't (line 542) | may use names from earlier examples |
| `examples/10_try-it-yourself.py` | Try it yourself (line 596) | runs on its own |
