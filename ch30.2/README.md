# 30.2 - Aliases, auto(), Customizing, IntEnum and StrEnum

The code of the chapter **30.2 - Aliases, auto(), Customizing, IntEnum and StrEnum** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Explain how aliases, `@unique` and `auto()` decide the values of members.
- Write methods, a mix-in base, and truth and ordering rules on an enum.
- Choose between `IntEnum` and `StrEnum`, and say what their compatibility with `int` and `str` costs.

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_aliases.py` | Aliases (line 41) | runs on its own |
| `examples/02_aliases.py` | Aliases (line 60) | may use names from earlier examples |
| `examples/03_aliases.py` | Aliases (line 70) | may use names from earlier examples |
| `examples/04_aliases.py` | Aliases (line 82) | may use names from earlier examples |
| `examples/05_names-values-and-ordinary-attributes.py` | Aliases › Names, values and ordinary attributes (line 110) | runs on its own |
| `examples/06_names-values-and-ordinary-attributes.py` | Aliases › Names, values and ordinary attributes (line 149) | runs on its own |
| `examples/07_a-member-does-not-freeze-the-object-stored-as-it.py` | Aliases › A member does not freeze the object stored as its value (line 181) | runs on its own |
| `examples/08_automatic-values-with-auto.py` | Automatic values with `auto()` (line 230) | may use names from earlier examples |
| `examples/09_automatic-values-with-auto.py` | Automatic values with `auto()` (line 252) | may use names from earlier examples |
| `examples/10_use-the-generation-history-without-an-unbounded.py` | Automatic values with `auto()` › Use the generation history without an unbounded search (line 283) | runs on its own |
| `examples/11_use-the-generation-history-without-an-unbounded.py` | Automatic values with `auto()` › Use the generation history without an unbounded search (line 330) | runs on its own |
| `examples/12_use-names-when-values-have-no-outside-meaning.py` | Automatic values with `auto()` › Use names when values have no outside meaning (line 363) | runs on its own |
| `examples/13_customizing-and-extending-enums.py` | Customizing and extending enums (line 423) | may use names from earlier examples |
| `examples/14_customizing-and-extending-enums.py` | Customizing and extending enums (line 443) | may use names from earlier examples |
| `examples/15_customizing-and-extending-enums.py` | Customizing and extending enums (line 471) | runs on its own |
| `examples/16_choose-truth-and-ordering-rules-explicitly.py` | Customizing and extending enums › Choose truth and ordering rules explicitly (line 498) | runs on its own |
| `examples/17_choose-truth-and-ordering-rules-explicitly.py` | Customizing and extending enums › Choose truth and ordering rules explicitly (line 533) | runs on its own |
| `examples/18_choose-truth-and-ordering-rules-explicitly.py` | Customizing and extending enums › Choose truth and ordering rules explicitly (line 587) | runs on its own |
| `examples/19_intenum-when-you-need-number-behaviour.py` | `IntEnum`: when you need number behaviour (line 627) | may use names from earlier examples |
| `examples/20_integer-compatibility-can-collapse-distinct-keys.py` | `IntEnum`: when you need number behaviour › Integer compatibility can collapse distinct keys (line 656) | runs on its own |
| `examples/21_strenum-string-behaviour-3-11.py` | `StrEnum`: string behaviour (3.11+) (line 695) | may use names from earlier examples |
| `examples/22_try-it-yourself.py` | Try it yourself (line 746) | runs on its own |
