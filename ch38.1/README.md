# 38.1 - From Source Text to a Syntax Tree

The code of the chapter **38.1 - From Source Text to a Syntax Tree** of the Python tutorial (folder `05 - Runtime`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How Python turns source text into instructions and runs them
- Why a file with a syntax error never starts, while a runtime exception comes after earlier lines have run
- How to inspect tokens with the `tokenize` module and the syntax tree with the `ast` module
- Why parsing is not the final compilation check

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_preparing-a-whole-source-file-then-running-it.py` | Preparing a whole source file, then running it (line 79) | raises an error on purpose |
| `examples/02_preparing-a-whole-source-file-then-running-it.py` | Preparing a whole source file, then running it (line 95) | raises an error on purpose |
| `examples/03_tokenizing-splitting-source-into-tokens.py` | Tokenizing: splitting source into tokens (line 120) | may use names from earlier examples |
| `examples/04_logical-lines-and-indentation-carry-different-in.py` | Tokenizing: splitting source into tokens › Logical lines and indentation carry different information (line 162) | runs on its own |
| `examples/05_the-ast-source-structure-without-the-punctuation.py` | The AST: source structure without the punctuation (line 210) | may use names from earlier examples |
| `examples/06_parsing-is-not-the-final-compilation-check.py` | The AST: source structure without the punctuation › Parsing is not the final compilation check (line 249) | runs on its own |
| `examples/07_try-it-yourself.py` | Try it yourself (line 297) | runs on its own |
