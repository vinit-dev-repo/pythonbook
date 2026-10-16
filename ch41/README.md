# 41 - Specialized Dictionaries

The code of the chapter **41 - Specialized Dictionaries** of the Python tutorial (folder `06 - Containers and data boundaries`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why the `collections` module exists and when to use it instead of `dict`
- How `defaultdict` creates values for missing keys, and how a read can change it
- What `OrderedDict` can do beyond the insertion order of `dict`
- `Counter` — counting things in one line, plus arithmetic between counts
- `ChainMap` — searching several dictionaries as if they were one
- `UserDict` — a base for custom mappings, with operation-specific limits
- `MappingProxyType` — a read-only window onto a dictionary you do not want changed

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `nested_config_lab.py` | ChainMap — searching several dictionaries as one › Build nested configuration views (line 613) |  |
| `normalized_mapping_lab.py` | UserDict — a class made for custom mappings › Give supported operations one key policy (line 829) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_why-the-collections-module-exists.py` | Why the collections module exists (line 46) | runs on its own |
| `examples/02_recognize-the-mapping-interface.py` | Why the collections module exists › Recognize the mapping interface (line 60) | runs on its own |
| `examples/03_defaultdict-dictionaries-that-fill-in-missing-ke.py` | defaultdict — dictionaries that fill in missing keys (line 90) | may use names from earlier examples |
| `examples/04_the-classic-group-by-example-in-three-lines.py` | defaultdict — dictionaries that fill in missing keys › The classic group-by example, in three lines (line 124) | may use names from earlier examples |
| `examples/05_the-warning-reading-a-key-creates-it.py` | defaultdict — dictionaries that fill in missing keys › The warning: reading a key CREATES it (line 152) | may use names from earlier examples |
| `examples/06_the-warning-reading-a-key-creates-it.py` | defaultdict — dictionaries that fill in missing keys › The warning: reading a key CREATES it (line 170) | may use names from earlier examples |
| `examples/07_compare-a-read-with-an-insertion.py` | defaultdict — dictionaries that fill in missing keys › Compare a read with an insertion (line 197) | may use names from earlier examples |
| `examples/08_ordereddict-when-a-plain-dict-is-not-quite-enoug.py` | OrderedDict — when a plain dict is not quite enough (line 242) | may use names from earlier examples |
| `examples/09_ordereddict-when-a-plain-dict-is-not-quite-enoug.py` | OrderedDict — when a plain dict is not quite enough (line 274) | may use names from earlier examples |
| `examples/10_ordereddict-when-a-plain-dict-is-not-quite-enoug.py` | OrderedDict — when a plain dict is not quite enough (line 288) | may use names from earlier examples |
| `examples/11_counter-counting-anything-in-one-line.py` | Counter — counting anything in one line (line 314) | may use names from earlier examples |
| `examples/12_counter-counting-anything-in-one-line.py` | Counter — counting anything in one line (line 329) | may use names from earlier examples |
| `examples/13_arithmetic-between-counters.py` | Counter — counting anything in one line › Arithmetic between Counters (line 348) | may use names from earlier examples |
| `examples/14_arithmetic-between-counters.py` | Counter — counting anything in one line › Arithmetic between Counters (line 375) | may use names from earlier examples |
| `examples/15_keep-a-signed-balance-with-subtract.py` | Counter — counting anything in one line › Keep a signed balance with subtract (line 398) | may use names from earlier examples |
| `examples/16_keep-a-signed-balance-with-subtract.py` | Counter — counting anything in one line › Keep a signed balance with subtract (line 424) | may use names from earlier examples |
| `examples/17_elements-turning-counts-back-into-a-list.py` | Counter — counting anything in one line › elements() — turning counts back into a list (line 445) | may use names from earlier examples |
| `examples/18_worked-example-counting-words-in-a-sentence.py` | Counter — counting anything in one line › Worked example: counting words in a sentence (line 457) | may use names from earlier examples |
| `examples/19_chainmap-searching-several-dictionaries-as-one.py` | ChainMap — searching several dictionaries as one (line 495) | may use names from earlier examples |
| `examples/20_writes-go-to-the-first-map-only.py` | ChainMap — searching several dictionaries as one › Writes go to the FIRST map only (line 527) | may use names from earlier examples |
| `examples/21_new-child-adding-a-fresh-layer-for-a-new-scope.py` | ChainMap — searching several dictionaries as one › new_child() — adding a fresh layer for a new scope (line 557) | may use names from earlier examples |
| `examples/22_new-child-adding-a-fresh-layer-for-a-new-scope.py` | ChainMap — searching several dictionaries as one › new_child() — adding a fresh layer for a new scope (line 574) | may use names from earlier examples |
| `examples/23_userdict-a-class-made-for-custom-mappings.py` | UserDict — a class made for custom mappings (line 689) | may use names from earlier examples |
| `examples/24_userdict-a-class-made-for-custom-mappings.py` | UserDict — a class made for custom mappings (line 712) | may use names from earlier examples |
| `examples/25_a-caller-can-bypass-a-custom-read-too.py` | UserDict — a class made for custom mappings › A caller can bypass a custom read too (line 744) | may use names from earlier examples |
| `examples/26_check-each-write-path.py` | UserDict — a class made for custom mappings › Check each write path (line 790) | may use names from earlier examples |
| `examples/27_mappingproxytype-a-read-only-view-of-a-dict.py` | MappingProxyType — a read-only view of a dict (line 926) | may use names from earlier examples |
| `examples/28_class-dictionaries-use-a-mapping-proxy.py` | MappingProxyType — a read-only view of a dict › Class dictionaries use a mapping proxy (line 958) | may use names from earlier examples |
| `examples/29_exposing-a-read-only-view-of-your-own-internal-s.py` | MappingProxyType — a read-only view of a dict › Exposing a read-only view of your own internal state (line 977) | may use names from earlier examples |
| `examples/30_a-read-only-entry-can-still-refer-to-a-mutable-v.py` | MappingProxyType — a read-only view of a dict › A read-only entry can still refer to a mutable value (line 1020) | may use names from earlier examples |
| `examples/31_a-fixed-snapshot-instead-of-a-live-view-frozendi.py` | MappingProxyType — a read-only view of a dict › A fixed snapshot instead of a live view: `frozendict` (3.15) (line 1054) | may use names from earlier examples |
| `examples/32_try-it-yourself.py` | Try it yourself (line 1119) | may use names from earlier examples |
