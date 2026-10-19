# 39.2 - Creating Dictionaries, Safe Lookup, Removal, Views and Merging

The code of the chapter **39.2 - Creating Dictionaries, Safe Lookup, Removal, Views and Merging** of the Python tutorial (folder `06 - Containers and data boundaries`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Six common ways to build a dictionary
- How to use `get`, `setdefault`, `pop`, `popitem`, and the `__missing__` hook
- Why `keys()`, `values()` and `items()` are "views", not copies
- The right way to merge, update and copy dictionaries, and a shallow-copy trap

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `alias_lookup_lab.py` | Common operations, in depth › Give an alias lookup a stopping point (line 201) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_common-ways-to-create-a-dictionary.py` | Common ways to create a dictionary (line 49) | runs on its own |
| `examples/02_common-ways-to-create-a-dictionary.py` | Common ways to create a dictionary (line 86) | may use names from earlier examples |
| `examples/03_get-look-up-without-crashing.py` | Common operations, in depth › `get`: look up without crashing (line 130) | may use names from earlier examples |
| `examples/04_setdefault-get-but-also-insert-if-missing.py` | Common operations, in depth › `setdefault`: get, but also *insert* if missing (line 150) | may use names from earlier examples |
| `examples/05_missing-customize-bracket-lookup-in-a-dict-subcl.py` | Common operations, in depth › `__missing__`: customize bracket lookup in a dict subclass (line 172) | may use names from earlier examples |
| `examples/06_del-pop-and-popitem-three-ways-to-remove.py` | Common operations, in depth › `del`, `pop` and `popitem`: three ways to remove (line 264) | may use names from earlier examples |
| `examples/07_in-checking-membership.py` | Common operations, in depth › `in`: checking membership (line 288) | may use names from earlier examples |
| `examples/08_dictionary-views-live-windows-not-copies.py` | Dictionary views: live windows, not copies (line 313) | may use names from earlier examples |
| `examples/09_dictionary-views-live-windows-not-copies.py` | Dictionary views: live windows, not copies (line 331) | may use names from earlier examples |
| `examples/10_views-behave-like-sets.py` | Dictionary views: live windows, not copies › Views behave like sets (line 358) | may use names from earlier examples |
| `examples/11_iteration-order-is-guaranteed.py` | Dictionary views: live windows, not copies › Iteration order is guaranteed (line 377) | may use names from earlier examples |
| `examples/12_iteration-order-is-guaranteed.py` | Dictionary views: live windows, not copies › Iteration order is guaranteed (line 391) | may use names from earlier examples |
| `examples/13_iteration-order-is-guaranteed.py` | Dictionary views: live windows, not copies › Iteration order is guaranteed (line 410) | may use names from earlier examples |
| `examples/14_update-merge-another-dict-in-in-place.py` | Updating, merging and copying › `update()`: merge another dict in, in place (line 435) | may use names from earlier examples |
| `examples/15_and-merge-with-an-operator-python-3-9.py` | Updating, merging and copying › `\|` and `\|=`: merge with an operator (Python 3.9+) (line 452) | may use names from earlier examples |
| `examples/16_a-b-merging-by-unpacking.py` | Updating, merging and copying › `{**a, **b}`: merging by unpacking (line 476) | may use names from earlier examples |
| `examples/17_copy-is-shallow-the-nested-dict-surprise.py` | Updating, merging and copying › `copy()` is shallow: the nested-dict surprise (line 495) | may use names from earlier examples |
| `examples/18_copy-is-shallow-the-nested-dict-surprise.py` | Updating, merging and copying › `copy()` is shallow: the nested-dict surprise (line 514) | may use names from earlier examples |
| `examples/19_copy-is-shallow-the-nested-dict-surprise.py` | Updating, merging and copying › `copy()` is shallow: the nested-dict surprise (line 535) | may use names from earlier examples |
| `examples/20_try-it-yourself.py` | Try it yourself (line 597) | runs on its own |
