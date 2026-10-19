# 42.2 - Custom Decoding, JSON Schema, Shape Validators and Nested Data Views

The code of the chapter **42.2 - Custom Decoding, JSON Schema, Shape Validators and Nested Data Views** of the Python tutorial (folder `06 - Containers and data boundaries`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How to rebuild your own classes with custom decoders
- How to use a schema to reject invalid JSON before using it
- How to check nested data with a recursive validator, first with results and then with exceptions
- How to navigate nested data through attributes

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `person_boundary.py` | JSON schema, in plain words › Validate before constructing a Person (line 216) |  |
| `test_person_boundary.py` | JSON schema, in plain words › Validate before constructing a Person (line 274) |  |
| `exercise_person_boundary.py` | JSON schema, in plain words › Practice: keep the previous accepted Person (line 410) |  |
| `shape_result_lab.py` | Build a small recursive shape validator › First return a result from every level (line 483) |  |
| `shape_exception_lab.py` | Build a small recursive shape validator › Then let an exception travel through the calls (line 538) |  |
| `data_view_lab.py` | Explore nested data through attributes (line 629) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_object-hook.py` | Custom decoding: rebuilding your own objects › object_hook (line 43) | runs on its own |
| `examples/02_fix-2-mirrored-subclassing-jsondecoder.py` | Custom decoding: rebuilding your own objects › Fix 2, mirrored: subclassing JSONDecoder (line 80) | may use names from earlier examples |
| `examples/03_the-round-trip-a-person-survives-dumps-and-loads.py` | Custom decoding: rebuilding your own objects › The round-trip: a Person survives dumps and loads intact (line 120) | may use names from earlier examples |
| `examples/04_json-schema-in-plain-words.py` | JSON schema, in plain words (line 173) | may use names from earlier examples |
| `examples/05_try-it-yourself.py` | Try it yourself (line 740) | runs on its own |
