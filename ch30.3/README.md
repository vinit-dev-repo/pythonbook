# 30.3 - Flags, Choosing an Enum, match and an Error Catalog

The code of the chapter **30.3 - Flags, Choosing an Enum, match and an Error Catalog** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Combine choices with `IntFlag` and `Flag`, and tell them apart.
- Choose among an enum, a constant, a Boolean value and a string.
- Use enum members as `match` cases, and convert outside values before the match.
- Build an error catalog whose members carry a code, an exception type and a message.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `error_catalog.py` | Construct the catalog and preserve member identity (line 315) |  |
| `catalog_use.py` | Raise selected exceptions and inspect the catalog (line 471) |  |
| `catalog_metadata.py` | Raise selected exceptions and inspect the catalog › Member identity does not deeply freeze custom metadata (line 544) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_intflag-and-flag-combinable-bit-flags.py` | `IntFlag` and `Flag`: combinable bit flags (line 41) | runs on its own |
| `examples/02_no-flags-and-unknown-bits.py` | `IntFlag` and `Flag`: combinable bit flags › No flags and unknown bits (line 87) | runs on its own |
| `examples/03_before-after-order-status-strings-become-an-enum.py` | Decision table: enum vs the alternatives › Before/after: order status strings become an enum (line 153) | may use names from earlier examples |
| `examples/04_before-after-order-status-strings-become-an-enum.py` | Decision table: enum vs the alternatives › Before/after: order status strings become an enum (line 171) | may use names from earlier examples |
| `examples/05_before-after-order-status-strings-become-an-enum.py` | Decision table: enum vs the alternatives › Before/after: order status strings become an enum (line 200) | may use names from earlier examples |
| `examples/06_enums-for-states-categories-and-match-case.py` | Enums for states, categories, and `match`/`case` (line 227) | may use names from earlier examples |
| `examples/07_enums-for-states-categories-and-match-case.py` | Enums for states, categories, and `match`/`case` (line 264) | may use names from earlier examples |
| `examples/08_duplicate-codes-remain-errors-even-with-differen.py` | Construct the catalog and preserve member identity › Duplicate codes remain errors even with different metadata (line 380) | runs on its own |
| `examples/09_share-construction-without-sharing-members.py` | Construct the catalog and preserve member identity › Share construction without sharing members (line 414) | runs on its own |
| `examples/10_raise-selected-exceptions-and-inspect-the-catalo.py` | Raise selected exceptions and inspect the catalog (line 517) | runs on its own |
| `examples/11_try-it-yourself.py` | Try it yourself (line 609) | runs on its own |
