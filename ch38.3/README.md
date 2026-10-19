# 38.3 - Frames, Interpreter State, Exception Tables and Generators

The code of the chapter **38.3 - Frames, Interpreter State, Exception Tables and Generators** of the Python tutorial (folder `05 - Runtime`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How a traceback records the calls that led to an error
- Why some CPython builds limit threads with the GIL
- How an exception table replaced the old block stack
- How a generator pauses and resumes its work

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_frame-objects-the-context-bytecode-runs-in.py` | Frame objects: the context bytecode runs in (line 46) | runs on its own |
| `examples/02_execution-storage-and-an-inspectable-frame-are-d.py` | Frame objects: the context bytecode runs in › Execution storage and an inspectable frame are different layers (line 83) | runs on its own |
| `examples/03_linked-frames-form-the-call-stack.py` | Frame objects: the context bytecode runs in › Linked frames form the call stack (line 119) | raises an error on purpose |
| `examples/04_the-gil.py` | Interpreter state, thread state, and the GIL › The GIL (line 173) | may use names from earlier examples |
| `examples/05_the-block-stack-and-what-replaced-it.py` | The block stack, and what replaced it (line 215) | runs on its own |
| `examples/06_generators-a-frame-that-pauses-and-resumes.py` | Generators: a frame that pauses and resumes (line 293) | runs on its own |
| `examples/07_generators-a-frame-that-pauses-and-resumes.py` | Generators: a frame that pauses and resumes (line 327) | runs on its own |
| `examples/08_try-it-yourself.py` | Try it yourself (line 411) | runs on its own |
