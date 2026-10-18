# 22.4 - Operator Overloading with Mixed Types

The code of the chapter **22.4 - Operator Overloading with Mixed Types** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How Python picks the method that runs for `a + b`
- How `NotImplemented` differs from `NotImplementedError`
- How reflected methods make `2 * v` and `sum()` work
- How unary, in-place and matrix operators work
- How `__eq__` and the ordering methods handle mixed types

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_how-python-picks-which-method-runs-for-a-b.py` | Operator overloading with mixed types › How Python picks which method runs for `a + b` (line 52) | runs on its own |
| `examples/02_notimplemented-is-not-notimplementederror.py` | Operator overloading with mixed types › `NotImplemented` is not `NotImplementedError` (line 89) | may use names from earlier examples |
| `examples/03_refusal-absence-and-exceptions.py` | Operator overloading with mixed types › Refusal, absence, and exceptions (line 110) | may use names from earlier examples |
| `examples/04_reflected-operators-making-the-right-hand-side-w.py` | Operator overloading with mixed types › Reflected operators: making the right-hand side work too (line 184) | may use names from earlier examples |
| `examples/05_reflected-operators-making-the-right-hand-side-w.py` | Operator overloading with mixed types › Reflected operators: making the right-hand side work too (line 211) | may use names from earlier examples |
| `examples/06_reflected-operators-making-the-right-hand-side-w.py` | Operator overloading with mixed types › Reflected operators: making the right-hand side work too (line 242) | may use names from earlier examples |
| `examples/07_reflected-operators-making-the-right-hand-side-w.py` | Operator overloading with mixed types › Reflected operators: making the right-hand side work too (line 271) | may use names from earlier examples |
| `examples/08_returning-a-wrapper-without-nesting-wrappers.py` | Operator overloading with mixed types › Returning a wrapper without nesting wrappers (line 311) | may use names from earlier examples |
| `examples/09_subtraction-and-division-order-matters.py` | Operator overloading with mixed types › Subtraction and division: order matters (line 362) | may use names from earlier examples |
| `examples/10_unary-operators-neg-pos-abs-invert.py` | Operator overloading with mixed types › Unary operators: `__neg__`, `__pos__`, `__abs__`, `__invert__` (line 403) | may use names from earlier examples |
| `examples/11_unary-plus-can-apply-a-type-specific-rule.py` | Operator overloading with mixed types › Unary plus can apply a type-specific rule (line 453) | may use names from earlier examples |
| `examples/12_unary-plus-can-apply-a-type-specific-rule.py` | Operator overloading with mixed types › Unary plus can apply a type-specific rule (line 469) | may use names from earlier examples |
| `examples/13_in-place-operators-iadd-and-friends.py` | Operator overloading with mixed types › In-place operators: `__iadd__` and friends (line 493) | may use names from earlier examples |
| `examples/14_in-place-operators-iadd-and-friends.py` | Operator overloading with mixed types › In-place operators: `__iadd__` and friends (line 519) | may use names from earlier examples |
| `examples/15_following-aliases-through-augmented-assignment.py` | Operator overloading with mixed types › Following aliases through augmented assignment (line 555) | may use names from earlier examples |
| `examples/16_finishing-eq-notimplemented-applies-to-equality.py` | Operator overloading with mixed types › Finishing `__eq__`: `NotImplemented` applies to equality too (line 618) | may use names from earlier examples |
| `examples/17_finishing-eq-notimplemented-applies-to-equality.py` | Operator overloading with mixed types › Finishing `__eq__`: `NotImplemented` applies to equality too (line 640) | may use names from earlier examples |
| `examples/18_finishing-eq-notimplemented-applies-to-equality.py` | Operator overloading with mixed types › Finishing `__eq__`: `NotImplemented` applies to equality too (line 665) | may use names from earlier examples |
| `examples/19_reflected-comparisons-use-opposite-questions.py` | Operator overloading with mixed types › Reflected comparisons use opposite questions (line 702) | may use names from earlier examples |
| `examples/20_matmul-and-the-operator.py` | Operator overloading with mixed types › `__matmul__` and the `@` operator (line 762) | may use names from earlier examples |
| `examples/21_try-it-yourself.py` | Try it yourself (line 819) | may use names from earlier examples |
