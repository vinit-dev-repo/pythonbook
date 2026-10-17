# 11.1 - Modules, the Standard Library and Packages

The code of the chapter **11.1 - Modules, the Standard Library and Packages** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What a module is, and the different ways to `import` one
- What Python's standard library gives you for free
- How to write your own module, and what happens the moment a file is imported
- The `if __name__ == "__main__":` line and `sys.argv`
- What a package is

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

The chapter saves these files more than once (for example a first version and a repaired one). This folder holds the version the chapter ends with, and the table points to that last version:

- `greetings.py`
- `main.py`

| File | Where it is in the chapter | Note |
|---|---|---|
| `noisy.py` | Writing your own module › What happens on import: initialization and reuse (line 142) |  |
| `main.py` | Writing your own module › What happens on import: initialization and reuse (line 150) | rewritten later in the chapter |
| `greetings.py` | Writing your own module › `if __name__ == "__main__":` (line 181) | rewritten later in the chapter |
| `greet.py` | Writing your own module › Command-line arguments (line 221) |  |
| `shop/__init__.py` | What a package is (line 309) |  |
| `shop/pricing.py` | What a package is (line 313) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_what-a-module-is.py` | What a module is (line 43) | runs on its own |
| `examples/02_the-four-ways-to-import.py` | What a module is › The four ways to import (line 66) | may use names from earlier examples |
| `examples/03_what-a-package-is.py` | What a package is (line 322) | runs on its own |
| `examples/04_try-it-yourself.py` | Try it yourself (line 361) | may use names from earlier examples |
