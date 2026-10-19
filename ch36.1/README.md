# 36.1 - Cleanup, try and finally, with and Writing a Manager Class

The code of the chapter **36.1 - Cleanup, try and finally, with and Writing a Manager Class** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why a program must release resources after success or failure
- How `try`/`finally` guarantees cleanup
- How the `with` statement manages setup and cleanup
- How `with` calls `__enter__` and `__exit__`, and how it relates to `try`/`finally`
- How to write your own context manager class

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_try-finally-the-manual-way.py` | `try`/`finally`: the manual way (line 59) | raises an error on purpose |
| `examples/02_with-the-same-guarantee-packaged.py` | `with`: the same guarantee, packaged (line 92) | may use names from earlier examples |
| `examples/03_what-with-really-does.py` | What `with` really does (line 121) | may use names from earlier examples |
| `examples/04_writing-your-own-context-manager-class.py` | Writing your own context manager class (line 185) | may use names from earlier examples |
| `examples/05_writing-your-own-context-manager-class.py` | Writing your own context manager class (line 202) | may use names from earlier examples |
| `examples/06_writing-your-own-context-manager-class.py` | Writing your own context manager class (line 222) | may use names from earlier examples |
| `examples/07_writing-your-own-context-manager-class.py` | Writing your own context manager class (line 250) | may use names from earlier examples |
| `examples/08_try-it-yourself.py` | Try it yourself (line 294) | runs on its own |
