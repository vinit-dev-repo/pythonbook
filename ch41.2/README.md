# 41.2 - ChainMap, UserDict, MappingProxyType and Choosing a Tool

The code of the chapter **41.2 - ChainMap, UserDict, MappingProxyType and Choosing a Tool** of the Python tutorial (folder `06 - Containers and data boundaries`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- `ChainMap`: searching several dictionaries as if they were one
- `UserDict`: a base for custom mappings, with operation-specific limits
- `MappingProxyType`: a read-only window onto a dictionary you do not want changed
- How to pick the right tool for a job

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `nested_config_lab.py` | ChainMap: searching several dictionaries as one › Build nested configuration views (line 152) |  |
| `normalized_mapping_lab.py` | UserDict: a class made for custom mappings › Give supported operations one key policy (line 363) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_chainmap-searching-several-dictionaries-as-one.py` | ChainMap: searching several dictionaries as one (line 42) | runs on its own |
| `examples/02_writes-go-to-the-first-map-only.py` | ChainMap: searching several dictionaries as one › Writes go to the FIRST map only (line 73) | may use names from earlier examples |
| `examples/03_new-child-adding-a-fresh-layer-for-a-new-scope.py` | ChainMap: searching several dictionaries as one › new_child(): adding a fresh layer for a new scope (line 100) | may use names from earlier examples |
| `examples/04_new-child-adding-a-fresh-layer-for-a-new-scope.py` | ChainMap: searching several dictionaries as one › new_child(): adding a fresh layer for a new scope (line 116) | may use names from earlier examples |
| `examples/05_userdict-a-class-made-for-custom-mappings.py` | UserDict: a class made for custom mappings (line 230) | may use names from earlier examples |
| `examples/06_userdict-a-class-made-for-custom-mappings.py` | UserDict: a class made for custom mappings (line 252) | may use names from earlier examples |
| `examples/07_a-caller-can-bypass-a-custom-read-too.py` | UserDict: a class made for custom mappings › A caller can bypass a custom read too (line 282) | may use names from earlier examples |
| `examples/08_check-each-write-path.py` | UserDict: a class made for custom mappings › Check each write path (line 328) | may use names from earlier examples |
| `examples/09_mappingproxytype-a-read-only-view-of-a-dict.py` | MappingProxyType: a read-only view of a dict (line 463) | may use names from earlier examples |
| `examples/10_class-dictionaries-use-a-mapping-proxy.py` | MappingProxyType: a read-only view of a dict › Class dictionaries use a mapping proxy (line 493) | may use names from earlier examples |
| `examples/11_exposing-a-read-only-view-of-your-own-internal-s.py` | MappingProxyType: a read-only view of a dict › Exposing a read-only view of your own internal state (line 510) | may use names from earlier examples |
| `examples/12_a-read-only-entry-can-still-refer-to-a-mutable-v.py` | MappingProxyType: a read-only view of a dict › A read-only entry can still refer to a mutable value (line 550) | may use names from earlier examples |
| `examples/13_a-fixed-snapshot-instead-of-a-live-view-frozendi.py` | MappingProxyType: a read-only view of a dict › A fixed snapshot instead of a live view: `frozendict` (3.15) (line 580) | may use names from earlier examples |
| `examples/14_try-it-yourself.py` | Try it yourself (line 650) | runs on its own |
