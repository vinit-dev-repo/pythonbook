# 14.2 - Encoding Errors, Source Files and Evidence

The code of the chapter **14.2 - Encoding Errors, Source Files and Evidence** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What `UnicodeEncodeError` and `UnicodeDecodeError` each mean
- How the `errors=` handlers decide what happens when a character will not fit
- How Python decodes a source file, and what a coding cookie does
- Why bytes do not reveal their encoding, and why a detector only proposes one

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `literal_encodings.py` | Python source files have an encoding › A literal, a display and encoded text are different (line 210) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_unicodeencodeerror-and-unicodedecodeerror.py` | UnicodeEncodeError and UnicodeDecodeError (line 42) | runs on its own |
| `examples/02_unicodeencodeerror-and-unicodedecodeerror.py` | UnicodeEncodeError and UnicodeDecodeError (line 57) | may use names from earlier examples |
| `examples/03_unicodeencodeerror-and-unicodedecodeerror.py` | UnicodeEncodeError and UnicodeDecodeError (line 72) | may use names from earlier examples |
| `examples/04_the-errors-handlers.py` | The errors= handlers (line 118) | may use names from earlier examples |
| `examples/05_the-errors-handlers.py` | The errors= handlers (line 146) | may use names from earlier examples |
| `examples/06_python-source-files-have-an-encoding.py` | Python source files have an encoding (line 180) | runs on its own |
| `examples/07_bytes-do-not-reveal-their-encoding.py` | Bytes do not reveal their encoding (line 255) | runs on its own |
| `examples/08_a-detector-proposes-an-interpretation.py` | Bytes do not reveal their encoding › A detector proposes an interpretation (line 280) | may use names from earlier examples |
| `examples/09_try-it-yourself.py` | Try it yourself (line 331) | may use names from earlier examples |
