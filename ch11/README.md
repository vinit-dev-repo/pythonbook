# 11 - Modules, Packages and Files

The code of the chapter **11 - Modules, Packages and Files** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What a module is, and the different ways to `import` one
- What Python's standard library gives you for free
- How to write your own module and use it from another file
- What actually happens the moment a file is imported
- The `if __name__ == "__main__":` line, explained slowly
- How to read command-line arguments with `sys.argv`
- What a package is
- How to open, read and write text files safely with `with`
- The difference between an absolute and a relative file path
- The modern way to work with paths: `pathlib`

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

The chapter saves these files more than once (for example a first version and a repaired one). This folder holds the version the chapter ends with, and the table points to that last version:

- `greetings.py`
- `main.py`

| File | Where it is in the chapter | Note |
|---|---|---|
| `noisy.py` | What happens on import: initialization and reuse (line 147) |  |
| `main.py` | What happens on import: initialization and reuse (line 155) | rewritten later in the chapter |
| `greetings.py` | `if __name__ == "__main__":` (line 190) | rewritten later in the chapter |
| `greet.py` | Command-line arguments (line 232) |  |
| `shop/__init__.py` | What a package is (line 320) |  |
| `shop/pricing.py` | What a package is (line 324) |  |
| `write_counts.py` | Practice: pass a file between two programs (line 710) |  |
| `read_counts.py` | Practice: pass a file between two programs (line 719) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_what-a-module-is.py` | What a module is (line 49) | runs on its own |
| `examples/02_the-four-ways-to-import.py` | The four ways to import (line 74) | may use names from earlier examples |
| `examples/03_what-a-package-is.py` | What a package is (line 333) | runs on its own |
| `examples/04_opening-and-closing.py` | Opening and closing (line 359) | may use names from earlier examples |
| `examples/05_the-with-statement-the-safe-way.py` | The `with` statement: the safe way (line 374) | may use names from earlier examples |
| `examples/06_reading-a-file.py` | Reading a file (line 391) | may use names from earlier examples |
| `examples/07_reading-a-file.py` | Reading a file (line 408) | may use names from earlier examples |
| `examples/08_writing-w-overwrites-a-appends.py` | Writing: `"w"` overwrites, `"a"` appends (line 443) | may use names from earlier examples |
| `examples/09_send-printed-text-to-an-open-file.py` | Send printed text to an open file (line 479) | may use names from earlier examples |
| `examples/10_read-sizes-blank-lines-and-the-end-of-a-file.py` | Read sizes, blank lines and the end of a file (line 511) | may use names from earlier examples |
| `examples/11_bytes-update-modes-and-flushing.py` | Bytes, update modes and flushing (line 568) | may use names from earlier examples |
| `examples/12_absolute-and-relative-file-paths.py` | Absolute and relative file paths (line 627) | runs on its own |
| `examples/13_working-with-paths-by-using-pathlib.py` | Working with paths by using `pathlib` (line 657) | may use names from earlier examples |
| `examples/14_working-with-paths-by-using-pathlib.py` | Working with paths by using `pathlib` (line 674) | may use names from earlier examples |
| `examples/15_try-it-yourself.py` | Try it yourself (line 779) | may use names from earlier examples |
