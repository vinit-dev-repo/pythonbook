# 08 - Comprehensions

The code of the chapter **08 - Comprehensions** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- The idea behind a comprehension: turning a build-a-list loop into one readable line
- The exact anatomy of a list comprehension, piece by piece
- Adding a condition (filtering) and a transform (changing each item)
- Nested loops inside a comprehension, and when that becomes unreadable
- Dict comprehensions and set comprehensions
- How a generator expression produces items on demand and is consumed once
- When NOT to use a comprehension

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_the-idea-a-loop-in-one-line.py` | The idea: a loop in one line (line 40) | runs on its own |
| `examples/02_the-idea-a-loop-in-one-line.py` | The idea: a loop in one line (line 57) | may use names from earlier examples |
| `examples/03_the-loop-name-stays-inside-the-comprehension.py` | The idea: a loop in one line › The loop name stays inside the comprehension (line 77) | may use names from earlier examples |
| `examples/04_the-loop-name-stays-inside-the-comprehension.py` | The idea: a loop in one line › The loop name stays inside the comprehension (line 94) | may use names from earlier examples |
| `examples/05_anatomy-of-a-list-comprehension.py` | Anatomy of a list comprehension (line 134) | may use names from earlier examples |
| `examples/06_with-both-a-transform-and-a-condition.py` | Anatomy of a list comprehension › With both a transform and a condition (line 154) | may use names from earlier examples |
| `examples/07_with-both-a-transform-and-a-condition.py` | Anatomy of a list comprehension › With both a transform and a condition (line 195) | may use names from earlier examples |
| `examples/08_with-both-a-transform-and-a-condition.py` | Anatomy of a list comprehension › With both a transform and a condition (line 214) | may use names from earlier examples |
| `examples/09_nested-loops-inside-a-comprehension.py` | Nested loops inside a comprehension (line 235) | may use names from earlier examples |
| `examples/10_nested-loops-inside-a-comprehension.py` | Nested loops inside a comprehension (line 249) | may use names from earlier examples |
| `examples/11_keep-rows-separate-or-collect-their-values.py` | Nested loops inside a comprehension › Keep rows separate or collect their values (line 268) | may use names from earlier examples |
| `examples/12_keep-rows-separate-or-collect-their-values.py` | Nested loops inside a comprehension › Keep rows separate or collect their values (line 274) | may use names from earlier examples |
| `examples/13_keep-rows-separate-or-collect-their-values.py` | Nested loops inside a comprehension › Keep rows separate or collect their values (line 289) | may use names from earlier examples |
| `examples/14_keep-rows-separate-or-collect-their-values.py` | Nested loops inside a comprehension › Keep rows separate or collect their values (line 301) | may use names from earlier examples |
| `examples/15_keep-rows-separate-or-collect-their-values.py` | Nested loops inside a comprehension › Keep rows separate or collect their values (line 318) | may use names from earlier examples |
| `examples/16_keep-rows-separate-or-collect-their-values.py` | Nested loops inside a comprehension › Keep rows separate or collect their values (line 330) | may use names from earlier examples |
| `examples/17_keep-rows-separate-or-collect-their-values.py` | Nested loops inside a comprehension › Keep rows separate or collect their values (line 342) | may use names from earlier examples |
| `examples/18_keep-rows-separate-or-collect-their-values.py` | Nested loops inside a comprehension › Keep rows separate or collect their values (line 362) | may use names from earlier examples |
| `examples/19_unpack-each-row-with-3-15.py` | Nested loops inside a comprehension › Unpack each row with `*` (3.15) (line 386) | a fragment, not a complete program |
| `examples/20_unpack-each-row-with-3-15.py` | Nested loops inside a comprehension › Unpack each row with `*` (3.15) (line 399) | a fragment, not a complete program |
| `examples/21_dict-comprehensions.py` | Dict comprehensions (line 423) | may use names from earlier examples |
| `examples/22_dict-comprehensions.py` | Dict comprehensions (line 436) | may use names from earlier examples |
| `examples/23_dict-comprehensions.py` | Dict comprehensions (line 453) | may use names from earlier examples |
| `examples/24_dict-comprehensions.py` | Dict comprehensions (line 472) | may use names from earlier examples |
| `examples/25_dict-comprehensions.py` | Dict comprehensions (line 490) | may use names from earlier examples |
| `examples/26_set-comprehensions.py` | Set comprehensions (line 512) | may use names from earlier examples |
| `examples/27_keeping-a-value-from-inside-the-walrus.py` | Keeping a value from inside: the walrus `:=` (line 541) | may use names from earlier examples |
| `examples/28_keeping-a-value-from-inside-the-walrus.py` | Keeping a value from inside: the walrus `:=` (line 558) | may use names from earlier examples |
| `examples/29_when-not-to-use-a-comprehension.py` | When NOT to use a comprehension (line 584) | may use names from earlier examples |
| `examples/30_generator-expressions.py` | Generator expressions (line 607) | may use names from earlier examples |
| `examples/31_generator-expressions.py` | Generator expressions (line 621) | may use names from earlier examples |
| `examples/32_practice-choose-the-tool-from-the-result-you-nee.py` | Practice: choose the tool from the result you need (line 664) | runs on its own |
| `examples/33_practice-choose-the-tool-from-the-result-you-nee.py` | Practice: choose the tool from the result you need (line 695) | runs on its own |
| `examples/34_try-it-yourself.py` | Try it yourself (line 766) | may use names from earlier examples |
