# 30 - Enums

The code of the chapter **30 - Enums** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why repeated unexplained numbers and strings can cause bugs
- How to define an **enumeration**, or enum, with `class ... (Enum)`
- What **singleton** means for an enum member, and why a plain enum member is not equal to its raw value
- How to find an enum member by its name or value
- Aliases, `auto()`, and writing your own methods on an enum
- When to use the special enum types `IntEnum`, `StrEnum`, and `IntFlag`
- How to choose among an enum, constant, Boolean value, and string

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `error_catalog.py` | Construct the catalog and preserve member identity (line 1235) |  |
| `catalog_use.py` | Raise selected exceptions and inspect the catalog (line 1391) |  |
| `catalog_metadata.py` | Raise selected exceptions and inspect the catalog › Member identity does not deeply freeze custom metadata (line 1466) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_why-enums-help.py` | Why enums help (line 51) | runs on its own |
| `examples/02_why-enums-help.py` | Why enums help (line 57) | may use names from earlier examples |
| `examples/03_why-enums-help.py` | Why enums help (line 65) | may use names from earlier examples |
| `examples/04_creating-an-enum.py` | Creating an Enum (line 94) | may use names from earlier examples |
| `examples/05_creating-an-enum.py` | Creating an Enum (line 124) | may use names from earlier examples |
| `examples/06_members-are-singletons.py` | Members are singletons (line 143) | may use names from earlier examples |
| `examples/07_why-comparing-with-the-raw-value-fails.py` | Members are singletons › Why comparing with the raw value fails (line 166) | may use names from earlier examples |
| `examples/08_enums-are-iterable-and-hashable.py` | Enums are iterable and hashable (line 190) | may use names from earlier examples |
| `examples/09_enums-are-iterable-and-hashable.py` | Enums are iterable and hashable (line 202) | may use names from earlier examples |
| `examples/10_lookup-both-directions.py` | Lookup both directions (line 226) | may use names from earlier examples |
| `examples/11_lookup-both-directions.py` | Lookup both directions (line 246) | may use names from earlier examples |
| `examples/12_aliases.py` | Aliases (line 280) | may use names from earlier examples |
| `examples/13_aliases.py` | Aliases (line 298) | may use names from earlier examples |
| `examples/14_aliases.py` | Aliases (line 309) | may use names from earlier examples |
| `examples/15_aliases.py` | Aliases (line 322) | may use names from earlier examples |
| `examples/16_names-values-and-ordinary-attributes.py` | Aliases › Names, values and ordinary attributes (line 351) | runs on its own |
| `examples/17_names-values-and-ordinary-attributes.py` | Aliases › Names, values and ordinary attributes (line 390) | runs on its own |
| `examples/18_a-member-does-not-freeze-the-object-stored-as-it.py` | Aliases › A member does not freeze the object stored as its value (line 424) | runs on its own |
| `examples/19_automatic-values-with-auto.py` | Automatic values with `auto()` (line 470) | may use names from earlier examples |
| `examples/20_automatic-values-with-auto.py` | Automatic values with `auto()` (line 492) | may use names from earlier examples |
| `examples/21_use-the-generation-history-without-an-unbounded.py` | Automatic values with `auto()` › Use the generation history without an unbounded search (line 524) | runs on its own |
| `examples/22_use-the-generation-history-without-an-unbounded.py` | Automatic values with `auto()` › Use the generation history without an unbounded search (line 572) | runs on its own |
| `examples/23_use-names-when-values-have-no-outside-meaning.py` | Automatic values with `auto()` › Use names when values have no outside meaning (line 606) | runs on its own |
| `examples/24_customizing-and-extending-enums.py` | Customizing and extending enums (line 663) | may use names from earlier examples |
| `examples/25_customizing-and-extending-enums.py` | Customizing and extending enums (line 684) | may use names from earlier examples |
| `examples/26_customizing-and-extending-enums.py` | Customizing and extending enums (line 712) | runs on its own |
| `examples/27_choose-truth-and-ordering-rules-explicitly.py` | Customizing and extending enums › Choose truth and ordering rules explicitly (line 740) | runs on its own |
| `examples/28_choose-truth-and-ordering-rules-explicitly.py` | Customizing and extending enums › Choose truth and ordering rules explicitly (line 775) | runs on its own |
| `examples/29_choose-truth-and-ordering-rules-explicitly.py` | Customizing and extending enums › Choose truth and ordering rules explicitly (line 830) | runs on its own |
| `examples/30_intenum-when-you-need-number-behaviour.py` | `IntEnum`: when you need number behaviour (line 867) | may use names from earlier examples |
| `examples/31_integer-compatibility-can-collapse-distinct-keys.py` | `IntEnum`: when you need number behaviour › Integer compatibility can collapse distinct keys (line 898) | runs on its own |
| `examples/32_strenum-string-behaviour-3-11.py` | `StrEnum`: string behaviour (3.11+) (line 934) | may use names from earlier examples |
| `examples/33_intflag-and-flag-combinable-bit-flags.py` | `IntFlag` and `Flag`: combinable bit flags (line 964) | may use names from earlier examples |
| `examples/34_no-flags-and-unknown-bits.py` | `IntFlag` and `Flag`: combinable bit flags › No flags and unknown bits (line 1011) | runs on its own |
| `examples/35_before-after-order-status-strings-become-an-enum.py` | Decision table: enum vs the alternatives › Before/after: order status strings become an enum (line 1075) | may use names from earlier examples |
| `examples/36_before-after-order-status-strings-become-an-enum.py` | Decision table: enum vs the alternatives › Before/after: order status strings become an enum (line 1094) | may use names from earlier examples |
| `examples/37_before-after-order-status-strings-become-an-enum.py` | Decision table: enum vs the alternatives › Before/after: order status strings become an enum (line 1124) | may use names from earlier examples |
| `examples/38_enums-for-states-categories-and-match-case.py` | Enums for states, categories, and `match`/`case` (line 1147) | may use names from earlier examples |
| `examples/39_enums-for-states-categories-and-match-case.py` | Enums for states, categories, and `match`/`case` (line 1185) | may use names from earlier examples |
| `examples/40_duplicate-codes-remain-errors-even-with-differen.py` | Construct the catalog and preserve member identity › Duplicate codes remain errors even with different metadata (line 1301) | runs on its own |
| `examples/41_share-construction-without-sharing-members.py` | Construct the catalog and preserve member identity › Share construction without sharing members (line 1336) | runs on its own |
| `examples/42_raise-selected-exceptions-and-inspect-the-catalo.py` | Raise selected exceptions and inspect the catalog (line 1437) | runs on its own |
| `examples/43_try-it-yourself.py` | Try it yourself (line 1532) | may use names from earlier examples |
