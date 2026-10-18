# 14.3 - The Unicode Sandwich, Files and Byte Order Marks

The code of the chapter **14.3 - The Unicode Sandwich, Files and Byte Order Marks** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- The Unicode sandwich: decode input, work in `str`, encode output
- How to open text files with `encoding=`, and why defaults differ between systems
- How text mode translates line endings, and how to inspect the encoding at each boundary
- The BOM, `utf-8-sig`, and the byte-order rule for UTF-16 streams

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `text_file_boundaries.py` | Reading and writing files with encoding= › Text mode also translates line endings (line 112) |  |
| `utf16_streams.py` | The BOM and utf-8-sig › UTF-16 streams need a byte-order rule (line 275) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_reading-and-writing-files-with-encoding.py` | Reading and writing files with encoding= (line 59) | runs on its own |
| `examples/02_reading-and-writing-files-with-encoding.py` | Reading and writing files with encoding= (line 82) | may use names from earlier examples |
| `examples/03_inspect-the-encoding-used-at-each-boundary.py` | Reading and writing files with encoding= › Inspect the encoding used at each boundary (line 164) | may use names from earlier examples |
| `examples/04_the-bom-and-utf-8-sig.py` | The BOM and utf-8-sig (line 223) | may use names from earlier examples |
| `examples/05_the-bom-and-utf-8-sig.py` | The BOM and utf-8-sig (line 236) | may use names from earlier examples |
| `examples/06_try-it-yourself.py` | Try it yourself (line 343) | may use names from earlier examples |

## Terminal commands

| File | Where it is in the chapter | Note |
|---|---|---|
| `commands/01_set-a-redirected-stream-s-encoding-before-launch.ps1` | Reading and writing files with encoding= › Set a redirected stream's encoding before launch (line 191) | powershell commands to type in a terminal |
