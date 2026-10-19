# 38.2 - Symbol Tables, Code Objects, Bytecode and the Stack Machine

The code of the chapter **38.2 - Symbol Tables, Code Objects, Bytecode and the Stack Machine** of the Python tutorial (folder `05 - Runtime`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Where each name lives: local, global or free, and how a closure shares a cell
- The difference between compiled instructions and the current state of a running function
- How to read a short instruction listing from `dis.dis()`
- How a stack machine passes temporary values from one instruction to the next

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_the-symbol-table-deciding-where-each-name-lives.py` | The symbol table: deciding where each name lives (line 43) | runs on its own |
| `examples/02_code-objects-the-compiled-result.py` | Code objects: the compiled result (line 118) | may use names from earlier examples |
| `examples/03_code-objects-the-compiled-result.py` | Code objects: the compiled result (line 167) | may use names from earlier examples |
| `examples/04_a-code-object-nested-inside-another.py` | Code objects: the compiled result › A code object nested inside another (line 200) | may use names from earlier examples |
| `examples/05_bytecode-and-dis-reading-the-compiled-instructio.py` | Bytecode and dis: reading the compiled instructions (line 260) | runs on its own |
| `examples/06_bytecode-and-dis-reading-the-compiled-instructio.py` | Bytecode and dis: reading the compiled instructions (line 297) | runs on its own |
| `examples/07_inspect-an-argument-that-needs-more-than-one-byt.py` | Bytecode and dis: reading the compiled instructions › Inspect an argument that needs more than one byte (line 342) | runs on its own |
| `examples/08_connect-instructions-back-to-source-locations.py` | Bytecode and dis: reading the compiled instructions › Connect instructions back to source locations (line 388) | runs on its own |
| `examples/09_from-branches-to-jump-targets.py` | Bytecode and dis: reading the compiled instructions › From branches to jump targets (line 432) | runs on its own |
| `examples/10_a-sampling-of-opcodes.py` | A sampling of opcodes (line 492) | runs on its own |
| `examples/11_the-stack-machine-how-a-b-really-runs.py` | The stack machine: how `a + b` really runs (line 562) | runs on its own |
| `examples/12_try-it-yourself.py` | Try it yourself (line 649) | runs on its own |
