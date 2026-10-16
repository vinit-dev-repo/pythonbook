# 39 - Hash Tables and Dictionaries in Depth

The code of the chapter **39 - Hash Tables and Dictionaries in Depth** of the Python tutorial (folder `06 - Containers and data boundaries`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What an "associative array" is, and why `dict` is Python's version of it
- How Python uses a hash table to store and find dictionary items
- What a hash collision is and how Python handles it
- Which values Python will let you use as dictionary keys, and why
- Six common ways to build a dictionary
- How to use `get`, `setdefault`, `pop`, `popitem`, and the `__missing__` hook
- Why `keys()`, `values()` and `items()` are "views", not copies
- The right way to merge, update and copy dictionaries — and a shallow-copy trap
- How to make your own classes usable as dictionary keys, safely

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `hash_bits_lab.py` | Observe hash bits without treating them as identifiers (line 162) |  |
| `alias_lookup_lab.py` | Give an alias lookup a stopping point (line 413) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_what-is-an-associative-array.py` | What is an associative array? (line 50) | runs on its own |
| `examples/02_python-s-hash-what-it-accepts-and-refuses.py` | Python's `hash()`: what it accepts and refuses (line 109) | may use names from earlier examples |
| `examples/03_python-s-hash-what-it-accepts-and-refuses.py` | Python's `hash()`: what it accepts and refuses (line 123) | raises an error on purpose |
| `examples/04_what-can-be-a-key-the-hashable-recap.py` | What can be a key: the hashable recap (line 227) | raises an error on purpose |
| `examples/05_common-ways-to-create-a-dictionary.py` | Common ways to create a dictionary (line 255) | may use names from earlier examples |
| `examples/06_common-ways-to-create-a-dictionary.py` | Common ways to create a dictionary (line 293) | may use names from earlier examples |
| `examples/07_get-look-up-without-crashing.py` | `get`: look up without crashing (line 336) | may use names from earlier examples |
| `examples/08_setdefault-get-but-also-insert-if-missing.py` | `setdefault`: get, but also *insert* if missing (line 358) | may use names from earlier examples |
| `examples/09_missing-customize-bracket-lookup-in-a-dict-subcl.py` | `__missing__`: customize bracket lookup in a dict subclass (line 382) | may use names from earlier examples |
| `examples/10_del-pop-and-popitem-three-ways-to-remove.py` | `del`, `pop` and `popitem`: three ways to remove (line 478) | may use names from earlier examples |
| `examples/11_in-checking-membership.py` | `in`: checking membership (line 503) | may use names from earlier examples |
| `examples/12_dictionary-views-live-windows-not-copies.py` | Dictionary views: live windows, not copies (line 527) | may use names from earlier examples |
| `examples/13_dictionary-views-live-windows-not-copies.py` | Dictionary views: live windows, not copies (line 546) | may use names from earlier examples |
| `examples/14_views-behave-like-sets.py` | Views behave like sets (line 576) | may use names from earlier examples |
| `examples/15_iteration-order-is-guaranteed.py` | Iteration order is guaranteed (line 597) | may use names from earlier examples |
| `examples/16_iteration-order-is-guaranteed.py` | Iteration order is guaranteed (line 612) | may use names from earlier examples |
| `examples/17_iteration-order-is-guaranteed.py` | Iteration order is guaranteed (line 632) | may use names from earlier examples |
| `examples/18_update-merge-another-dict-in-in-place.py` | `update()`: merge another dict in, in place (line 656) | may use names from earlier examples |
| `examples/19_and-merge-with-an-operator-python-3-9.py` | `\|` and `\|=`: merge with an operator (Python 3.9+) (line 675) | may use names from earlier examples |
| `examples/20_a-b-merging-by-unpacking.py` | `{**a, **b}`: merging by unpacking (line 702) | may use names from earlier examples |
| `examples/21_copy-is-shallow-the-nested-dict-surprise.py` | `copy()` is shallow — the nested-dict surprise (line 724) | may use names from earlier examples |
| `examples/22_copy-is-shallow-the-nested-dict-surprise.py` | `copy()` is shallow — the nested-dict surprise (line 745) | may use names from earlier examples |
| `examples/23_copy-is-shallow-the-nested-dict-surprise.py` | `copy()` is shallow — the nested-dict surprise (line 767) | may use names from earlier examples |
| `examples/24_using-your-own-classes-as-dictionary-keys.py` | Using your own classes as dictionary keys (line 810) | may use names from earlier examples |
| `examples/25_using-your-own-classes-as-dictionary-keys.py` | Using your own classes as dictionary keys (line 835) | may use names from earlier examples |
| `examples/26_why-a-key-s-hash-must-not-change.py` | Why a key's hash must not change (line 878) | may use names from earlier examples |
| `examples/27_use-coordinate-keys-for-sparse-data.py` | Use coordinate keys for sparse data (line 903) | may use names from earlier examples |
| `examples/28_reverse-lookup-can-return-several-keys.py` | Reverse lookup can return several keys (line 932) | may use names from earlier examples |
| `examples/29_practice-track-an-ordered-queue-of-jobs.py` | Practice: track an ordered queue of jobs (line 963) | may use names from earlier examples |
| `examples/30_try-it-yourself.py` | Try it yourself (line 1024) | may use names from earlier examples |
