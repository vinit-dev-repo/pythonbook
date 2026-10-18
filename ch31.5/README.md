# 31.5 - Display, Delegation and Tracing Wrappers

The code of the chapter **31.5 - Display, Delegation and Tracing Wrappers** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Compare display designs and say what a dictionary-based view leaves out.
- Inspect own fields, inherited values and class definitions, and map where a name is defined.
- Forward reads with `__getattr__`, and say why a write creates a local field on the wrapper.
- Trace lookups with a wrapper that has its own state, and say why it changes the exposed type.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `display_records.py` | Display and delegate a record (line 44) |  |
| `namespace_views.py` | Display and delegate a record › Inspect three kinds of namespace (line 186) |  |
| `inspection_tools.py` | Display and delegate a record › Inspect three kinds of namespace (line 273) |  |
| `try_views.py` | Display and delegate a record › Inspect three kinds of namespace (line 284) |  |
| `repr_loop.py` | Display and delegate a record › A display can call itself indirectly (line 381) |  |
| `inspection_transfer.py` | Display and delegate a record › Transfer: shared ancestors, slots and a library class (line 425) |  |
| `attribute_origins.py` | Display and delegate a record › Map definitions without reading their values (line 527) |  |
| `delegate_record.py` | Display and delegate a record › A wrapper forwards only the operations it implements (line 629) |  |
| `tracer_lab.py` | Trace a constructed target (line 719) |  |
| `class_factory_trace.py` | Trace a constructed target › A class factory can return a tracing wrapper (line 864) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_predict-which-fields-are-displayed.py` | Display and delegate a record › Predict which fields are displayed (line 144) | runs on its own |
| `examples/02_a-wrapper-forwards-only-the-operations-it-implem.py` | Display and delegate a record › A wrapper forwards only the operations it implements (line 682) | runs on its own |
| `examples/03_trace-a-constructed-target.py` | Trace a constructed target (line 784) | runs on its own |
| `examples/04_trace-a-constructed-target.py` | Trace a constructed target (line 802) | runs on its own |
| `examples/05_trace-a-constructed-target.py` | Trace a constructed target (line 837) | runs on its own |
| `examples/06_try-it-yourself.py` | Try it yourself (line 927) | runs on its own |
| `examples/07_2-find-the-problem.py` | 2. Find the problem (line 1032) | runs on its own |
| `examples/08_3-build.py` | 3. Build (line 1072) | runs on its own |
