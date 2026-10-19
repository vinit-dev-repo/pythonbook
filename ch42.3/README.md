# 42.3 - Related Tools, Typed Records, XML and Choosing a Format

The code of the chapter **42.3 - Related Tools, Typed Records, XML and Choosing a Format** of the Python tutorial (folder `06 - Containers and data boundaries`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How a `shelve` file keeps a dictionary on disk, and how properties follow stored references
- A quick tour of YAML and typed validation with `pydantic`
- How to keep dates and decimals typed inside a JSON document
- Reading and writing XML while keeping text, bytes and nested content distinct
- How to choose a format for a job

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `linked_archive.py` | Related serialization tools › Properties can follow stored references (line 91) |  |
| `linked_archive_demo.py` | Related serialization tools › Properties can follow stored references (line 185) |  |
| `workshop_json_lab.py` | Preserve typed records inside a document › A tagged format with a fixed registry (line 476) |  |
| `workshop_schema_lab.py` | Preserve typed records inside a document › Let schemas carry the type information instead (line 571) |  |
| `xml_records.py` | Parse XML with its structure intact (line 648) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_shelve-a-dictionary-that-lives-on-disk.py` | Related serialization tools › `shelve`: a dictionary that lives on disk (line 42) | runs on its own |
| `examples/02_pyyaml-human-friendly-configuration-files.py` | Related serialization tools › PyYAML: human-friendly configuration files (line 263) | may use names from earlier examples |
| `examples/03_pyyaml-human-friendly-configuration-files.py` | Related serialization tools › PyYAML: human-friendly configuration files (line 287) | may use names from earlier examples |
| `examples/04_marshmallow-schemas-that-serialize-and-validate.py` | Related serialization tools › Marshmallow: schemas that serialize AND validate (line 318) | may use names from earlier examples |
| `examples/05_serpy-a-historical-one-way-serializer.py` | Related serialization tools › Serpy: a historical one-way serializer (line 354) | may use names from earlier examples |
| `examples/06_serpy-a-historical-one-way-serializer.py` | Related serialization tools › Serpy: a historical one-way serializer (line 384) | may use names from earlier examples |
| `examples/07_serpy-a-historical-one-way-serializer.py` | Related serialization tools › Serpy: a historical one-way serializer (line 406) | runs on its own |
| `examples/08_try-it-yourself.py` | Try it yourself (line 741) | runs on its own |
