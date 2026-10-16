# 26a - Project - Composing Readers, Converters and Writers

The code of the chapter **26a - Project - Composing Readers, Converters and Writers** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Compose three small roles around one unchanged processing function.
- Separate a valid record from an explicit end-of-input marker.
- Substitute readers and writers without requiring a shared parent class.
- Test call order, false-valued records and the partial progress left by a failure.
- Compare a supplied converter function with a conversion method supplied by a subclass.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `processor.py` | Implement the interchangeable pieces (line 72) |  |
| `test_processor.py` | Check behavior across implementations and failures (line 163) |  |
| `processor_demo.py` | Trace real calls, then substitute the dependencies (line 395) |  |
| `processor_class.py` | Keep dependencies on an object (line 472) |  |
| `test_processor_class.py` | Keep dependencies on an object (line 540) |  |
| `processor_transfer.py` | Try it yourself (line 628) |  |
| `processor_class_transfer.py` | Try it yourself (line 680) |  |
