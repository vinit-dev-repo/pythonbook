# 38 - How Python Runs Your Code

The code of this chapter of the Python tutorial, extracted byte for byte from the certified chapter. The chapter explains every line; read it there.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

- `cache_validation_modes.py`
- `source_file_namespace.py`
- `sourceless_cache.py`
- `step1_first_import.py`
- `step3_edit_and_reimport.py`

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Section | Note |
|---|---|---|
| `examples/01_preparing-a-whole-source-file-then-running-it.py` | Preparing a whole source file, then running it | raises an error on purpose |
| `examples/02_preparing-a-whole-source-file-then-running-it.py` | Preparing a whole source file, then running it | raises an error on purpose |
| `examples/03_tokenizing-splitting-source-into-tokens.py` | Tokenizing: splitting source into tokens | may use names from earlier examples |
| `examples/04_logical-lines-and-indentation-carry-different-in.py` | Logical lines and indentation carry different information | runs on its own |
| `examples/05_the-ast-source-structure-without-the-punctuation.py` | The AST: source structure without the punctuation | may use names from earlier examples |
| `examples/06_parsing-is-not-the-final-compilation-check.py` | Parsing is not the final compilation check | runs on its own |
| `examples/07_the-symbol-table-deciding-where-each-name-lives.py` | The symbol table: deciding where each name lives | may use names from earlier examples |
| `examples/08_code-objects-the-compiled-result.py` | Code objects: the compiled result | may use names from earlier examples |
| `examples/09_code-objects-the-compiled-result.py` | Code objects: the compiled result | may use names from earlier examples |
| `examples/10_a-code-object-nested-inside-another.py` | A code object nested inside another | may use names from earlier examples |
| `examples/11_bytecode-and-dis-reading-the-compiled-instructio.py` | Bytecode and dis: reading the compiled instructions | runs on its own |
| `examples/12_bytecode-and-dis-reading-the-compiled-instructio.py` | Bytecode and dis: reading the compiled instructions | runs on its own |
| `examples/13_inspect-an-argument-that-needs-more-than-one-byt.py` | Inspect an argument that needs more than one byte | runs on its own |
| `examples/14_connect-instructions-back-to-source-locations.py` | Connect instructions back to source locations | runs on its own |
| `examples/15_from-branches-to-jump-targets.py` | From branches to jump targets | runs on its own |
| `examples/16_a-sampling-of-opcodes.py` | A sampling of opcodes | runs on its own |
| `examples/17_the-stack-machine-how-a-b-really-runs.py` | The stack machine: how `a + b` really runs | runs on its own |
| `examples/18_frame-objects-the-context-bytecode-runs-in.py` | Frame objects: the context bytecode runs in | may use names from earlier examples |
| `examples/19_execution-storage-and-an-inspectable-frame-are-d.py` | Execution storage and an inspectable frame are different layers | runs on its own |
| `examples/20_linked-frames-form-the-call-stack.py` | Linked frames form the call stack | raises an error on purpose |
| `examples/21_the-gil.py` | The GIL | may use names from earlier examples |
| `examples/22_the-block-stack-and-what-replaced-it.py` | The block stack — and what replaced it | runs on its own |
| `examples/23_generators-a-frame-that-pauses-and-resumes.py` | Generators: a frame that pauses and resumes | runs on its own |
| `examples/24_generators-a-frame-that-pauses-and-resumes.py` | Generators: a frame that pauses and resumes | runs on its own |
| `examples/25_pyc-files-and-pycache.py` | `.pyc` files and `__pycache__` | may use names from earlier examples |
| `examples/26_pyc-files-and-pycache.py` | `.pyc` files and `__pycache__` | runs on its own |
| `examples/27_a-class-body-also-has-compiled-code.py` | A class body also has compiled code | runs on its own |
| `examples/28_exec-and-eval-running-code-you-build-at-runtime.py` | `exec()` and `eval()`: running code you build at runtime | may use names from earlier examples |
| `examples/29_exec-and-eval-running-code-you-build-at-runtime.py` | `exec()` and `eval()`: running code you build at runtime | raises an error on purpose |
| `examples/30_future-opting-in-to-a-change-early.py` | `__future__`: opting in to a change early | runs on its own |
| `examples/31_future-opting-in-to-a-change-early.py` | `__future__`: opting in to a change early | may use names from earlier examples |
| `examples/32_constant-folding.py` | Constant folding | runs on its own |
| `examples/33_small-literal-sequences-get-folded-too-large-one.py` | Small literal sequences get folded too — large ones don't | may use names from earlier examples |
| `examples/34_try-it-yourself.py` | Try it yourself | runs on its own |
