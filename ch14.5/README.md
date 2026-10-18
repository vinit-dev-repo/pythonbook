# 14.5 - memoryview, Packed Records and Sorting Text

The code of the chapter **14.5 - memoryview, Packed Records and Sorting Text** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How a `memoryview` reads and changes existing bytes without copying them
- How to cast a view, make it read-only and release it
- How `struct` packs and unpacks a record with an explicit binary layout
- How code-point sorting, a limited search alias, locale collation and a versioned Unicode collation key differ

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `cast_buffer.py` | memoryview: reading bytes without copying them › Cast a view and release the buffer (line 102) |  |
| `packed_record.py` | Pack a record with an explicit binary layout (line 169) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_memoryview-reading-bytes-without-copying-them.py` | memoryview: reading bytes without copying them (line 43) | runs on its own |
| `examples/02_memoryview-reading-bytes-without-copying-them.py` | memoryview: reading bytes without copying them (line 77) | may use names from earlier examples |
| `examples/03_sorting-non-ascii-text.py` | Sorting non-ASCII text (line 225) | may use names from earlier examples |
| `examples/04_sorting-non-ascii-text.py` | Sorting non-ASCII text (line 240) | may use names from earlier examples |
| `examples/05_build-a-limited-search-alias-and-retain-the-orig.py` | Sorting non-ASCII text › Build a limited search alias and retain the original (line 269) | may use names from earlier examples |
| `examples/06_locale-collation-uses-installed-system-rules.py` | Sorting non-ASCII text › Locale collation uses installed system rules (line 315) | may use names from earlier examples |
| `examples/07_a-unicode-collation-key-has-a-data-version.py` | Sorting non-ASCII text › A Unicode collation key has a data version (line 342) | may use names from earlier examples |
| `examples/08_try-it-yourself.py` | Try it yourself (line 395) | may use names from earlier examples |
