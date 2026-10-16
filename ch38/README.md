# 38 - How Python Runs Your Code

The code of the chapter **38 - How Python Runs Your Code** of the Python tutorial (folder `05 - Runtime`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How Python turns source text into instructions and runs them
- How to inspect each stage with the `tokenize`, `ast`, `symtable`, and `dis` modules
- The difference between compiled instructions and the current state of a running function
- How to read a short instruction listing from `dis.dis()`
- How a traceback records the calls that led to an error
- Why some CPython builds limit threads with the GIL
- How a generator pauses and resumes its work
- What a `.pyc` file caches — and what it does NOT cache

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `step1_first_import.py` | `.pyc` files and `__pycache__` (line 1233) |  |
| `step3_edit_and_reimport.py` | `.pyc` files and `__pycache__` (line 1268) |  |
| `sourceless_cache.py` | A cached file without its source (line 1319) |  |
| `cache_validation_modes.py` | Timestamp checks and checked-hash caches (line 1370) |  |
| `source_file_namespace.py` | Executing a trusted source file in a chosen namespace (line 1535) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_preparing-a-whole-source-file-then-running-it.py` | Preparing a whole source file, then running it (line 91) | raises an error on purpose |
| `examples/02_preparing-a-whole-source-file-then-running-it.py` | Preparing a whole source file, then running it (line 107) | raises an error on purpose |
| `examples/03_tokenizing-splitting-source-into-tokens.py` | Tokenizing: splitting source into tokens (line 130) | may use names from earlier examples |
| `examples/04_logical-lines-and-indentation-carry-different-in.py` | Logical lines and indentation carry different information (line 176) | runs on its own |
| `examples/05_the-ast-source-structure-without-the-punctuation.py` | The AST: source structure without the punctuation (line 219) | may use names from earlier examples |
| `examples/06_parsing-is-not-the-final-compilation-check.py` | Parsing is not the final compilation check (line 262) | runs on its own |
| `examples/07_the-symbol-table-deciding-where-each-name-lives.py` | The symbol table: deciding where each name lives (line 294) | may use names from earlier examples |
| `examples/08_code-objects-the-compiled-result.py` | Code objects: the compiled result (line 366) | may use names from earlier examples |
| `examples/09_code-objects-the-compiled-result.py` | Code objects: the compiled result (line 416) | may use names from earlier examples |
| `examples/10_a-code-object-nested-inside-another.py` | A code object nested inside another (line 451) | may use names from earlier examples |
| `examples/11_bytecode-and-dis-reading-the-compiled-instructio.py` | Bytecode and dis: reading the compiled instructions (line 509) | runs on its own |
| `examples/12_bytecode-and-dis-reading-the-compiled-instructio.py` | Bytecode and dis: reading the compiled instructions (line 547) | runs on its own |
| `examples/13_inspect-an-argument-that-needs-more-than-one-byt.py` | Inspect an argument that needs more than one byte (line 594) | runs on its own |
| `examples/14_connect-instructions-back-to-source-locations.py` | Connect instructions back to source locations (line 640) | runs on its own |
| `examples/15_from-branches-to-jump-targets.py` | From branches to jump targets (line 681) | runs on its own |
| `examples/16_a-sampling-of-opcodes.py` | A sampling of opcodes (line 736) | runs on its own |
| `examples/17_the-stack-machine-how-a-b-really-runs.py` | The stack machine: how `a + b` really runs (line 804) | runs on its own |
| `examples/18_frame-objects-the-context-bytecode-runs-in.py` | Frame objects: the context bytecode runs in (line 873) | may use names from earlier examples |
| `examples/19_execution-storage-and-an-inspectable-frame-are-d.py` | Execution storage and an inspectable frame are different layers (line 907) | runs on its own |
| `examples/20_linked-frames-form-the-call-stack.py` | Linked frames form the call stack (line 944) | raises an error on purpose |
| `examples/21_the-gil.py` | The GIL (line 998) | may use names from earlier examples |
| `examples/22_the-block-stack-and-what-replaced-it.py` | The block stack — and what replaced it (line 1038) | runs on its own |
| `examples/23_generators-a-frame-that-pauses-and-resumes.py` | Generators: a frame that pauses and resumes (line 1110) | runs on its own |
| `examples/24_generators-a-frame-that-pauses-and-resumes.py` | Generators: a frame that pauses and resumes (line 1144) | runs on its own |
| `examples/25_pyc-files-and-pycache.py` | `.pyc` files and `__pycache__` (line 1214) | may use names from earlier examples |
| `examples/26_pyc-files-and-pycache.py` | `.pyc` files and `__pycache__` (line 1251) | runs on its own |
| `examples/27_a-class-body-also-has-compiled-code.py` | A class body also has compiled code (line 1423) | runs on its own |
| `examples/28_exec-and-eval-running-code-you-build-at-runtime.py` | `exec()` and `eval()`: running code you build at runtime (line 1472) | may use names from earlier examples |
| `examples/29_exec-and-eval-running-code-you-build-at-runtime.py` | `exec()` and `eval()`: running code you build at runtime (line 1504) | raises an error on purpose |
| `examples/30_future-opting-in-to-a-change-early.py` | `__future__`: opting in to a change early (line 1578) | runs on its own |
| `examples/31_future-opting-in-to-a-change-early.py` | `__future__`: opting in to a change early (line 1584) | may use names from earlier examples |
| `examples/32_constant-folding.py` | Constant folding (line 1678) | runs on its own |
| `examples/33_small-literal-sequences-get-folded-too-large-one.py` | Small literal sequences get folded too — large ones don't (line 1708) | may use names from earlier examples |
| `examples/34_try-it-yourself.py` | Try it yourself (line 1765) | runs on its own |
