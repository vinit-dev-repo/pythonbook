# 22 - Special Dunder Methods

The code of the chapter **22 - Special Dunder Methods** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What dunder methods are and which Python operations call them
- `__str__` vs `__repr__` — text for people vs text for developers
- Making your own objects work with `+`, `-`, `*`, `==`, `<`, and the other operators
- Why `__eq__` and `__hash__` must agree, and what breaks in dicts/sets if they don't
- `__bool__`, `__len__`, `__call__`, `__format__`, `__bytes__`, and `__index__`
- Why `__del__` should not be trusted for cleanup

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_what-dunder-methods-are.py` | What dunder methods are (line 59) | runs on its own |
| `examples/02_direct-lookup-and-implicit-lookup.py` | What dunder methods are › Direct lookup and implicit lookup (line 81) | may use names from earlier examples |
| `examples/03_str-vs-repr.py` | `__str__` vs `__repr__` (line 129) | may use names from earlier examples |
| `examples/04_display-does-not-define-a-reconstruction-format.py` | `__str__` vs `__repr__` › Display does not define a reconstruction format (line 167) | may use names from earlier examples |
| `examples/05_bytes-a-binary-representation.py` | `__bytes__`: a binary representation (line 198) | may use names from earlier examples |
| `examples/06_add-sub-mul.py` | Making objects work with operators › `__add__`, `__sub__`, `__mul__` (line 234) | may use names from earlier examples |
| `examples/07_eq-and-equality.py` | Making objects work with operators › `__eq__` and equality (line 276) | may use names from earlier examples |
| `examples/08_eq-and-equality.py` | Making objects work with operators › `__eq__` and equality (line 293) | may use names from earlier examples |
| `examples/09_the-other-comparisons.py` | Making objects work with operators › The other comparisons: `<`, `<=`, `>`, `>=` (line 335) | may use names from earlier examples |
| `examples/10_defining-eq-makes-instances-unhashable-by-defaul.py` | Hashing and equality: they must agree › Defining `__eq__` makes instances unhashable by default (line 387) | may use names from earlier examples |
| `examples/11_defining-eq-makes-instances-unhashable-by-defaul.py` | Hashing and equality: they must agree › Defining `__eq__` makes instances unhashable by default (line 413) | may use names from earlier examples |
| `examples/12_defining-eq-makes-instances-unhashable-by-defaul.py` | Hashing and equality: they must agree › Defining `__eq__` makes instances unhashable by default (line 443) | may use names from earlier examples |
| `examples/13_what-breaks-if-the-hash-disagrees-with-equality.py` | Hashing and equality: they must agree › What breaks if the hash disagrees with equality (line 478) | may use names from earlier examples |
| `examples/14_a-collision-is-not-an-equality-claim.py` | Hashing and equality: they must agree › A collision is not an equality claim (line 512) | may use names from earlier examples |
| `examples/15_bool-and-len.py` | `__bool__` and `__len__` (line 551) | may use names from earlier examples |
| `examples/16_bool-and-len.py` | `__bool__` and `__len__` (line 578) | may use names from earlier examples |
| `examples/17_default-truth-and-method-requirements.py` | `__bool__` and `__len__` › Default truth and method requirements (line 606) | may use names from earlier examples |
| `examples/18_call-objects-you-can-call-like-a-function.py` | `__call__`: objects you can call like a function (line 662) | may use names from earlier examples |
| `examples/19_format.py` | `__format__` (line 696) | may use names from earlier examples |
| `examples/20_forwarding-a-format-to-a-stored-value.py` | `__format__` › Forwarding a format to a stored value (line 723) | may use names from earlier examples |
| `examples/21_index-an-exact-integer-for-python-s-integer-only.py` | `__index__`: an exact integer for Python's integer-only operations (line 781) | may use names from earlier examples |
| `examples/22_exact-indices-differ-from-numeric-conversion.py` | `__index__`: an exact integer for Python's integer-only operations › Exact indices differ from numeric conversion (line 814) | may use names from earlier examples |
| `examples/23_how-python-picks-which-method-runs-for-a-b.py` | Operator overloading with mixed types › How Python picks which method runs for `a + b` (line 897) | may use names from earlier examples |
| `examples/24_notimplemented-is-not-notimplementederror.py` | Operator overloading with mixed types › `NotImplemented` is not `NotImplementedError` (line 935) | may use names from earlier examples |
| `examples/25_refusal-absence-and-exceptions.py` | Operator overloading with mixed types › Refusal, absence, and exceptions (line 958) | may use names from earlier examples |
| `examples/26_reflected-operators-making-the-right-hand-side-w.py` | Operator overloading with mixed types › Reflected operators: making the right-hand side work too (line 1036) | may use names from earlier examples |
| `examples/27_reflected-operators-making-the-right-hand-side-w.py` | Operator overloading with mixed types › Reflected operators: making the right-hand side work too (line 1064) | may use names from earlier examples |
| `examples/28_reflected-operators-making-the-right-hand-side-w.py` | Operator overloading with mixed types › Reflected operators: making the right-hand side work too (line 1096) | may use names from earlier examples |
| `examples/29_reflected-operators-making-the-right-hand-side-w.py` | Operator overloading with mixed types › Reflected operators: making the right-hand side work too (line 1126) | may use names from earlier examples |
| `examples/30_returning-a-wrapper-without-nesting-wrappers.py` | Operator overloading with mixed types › Returning a wrapper without nesting wrappers (line 1169) | may use names from earlier examples |
| `examples/31_subtraction-and-division-order-matters.py` | Operator overloading with mixed types › Subtraction and division: order matters (line 1224) | may use names from earlier examples |
| `examples/32_unary-operators-neg-pos-abs-invert.py` | Operator overloading with mixed types › Unary operators: `__neg__`, `__pos__`, `__abs__`, `__invert__` (line 1267) | may use names from earlier examples |
| `examples/33_unary-plus-can-apply-a-type-specific-rule.py` | Operator overloading with mixed types › Unary plus can apply a type-specific rule (line 1317) | may use names from earlier examples |
| `examples/34_unary-plus-can-apply-a-type-specific-rule.py` | Operator overloading with mixed types › Unary plus can apply a type-specific rule (line 1334) | may use names from earlier examples |
| `examples/35_in-place-operators-iadd-and-friends.py` | Operator overloading with mixed types › In-place operators: `__iadd__` and friends (line 1358) | may use names from earlier examples |
| `examples/36_in-place-operators-iadd-and-friends.py` | Operator overloading with mixed types › In-place operators: `__iadd__` and friends (line 1385) | may use names from earlier examples |
| `examples/37_following-aliases-through-augmented-assignment.py` | Operator overloading with mixed types › Following aliases through augmented assignment (line 1423) | may use names from earlier examples |
| `examples/38_finishing-eq-notimplemented-applies-to-equality.py` | Operator overloading with mixed types › Finishing `__eq__`: `NotImplemented` applies to equality too (line 1490) | may use names from earlier examples |
| `examples/39_finishing-eq-notimplemented-applies-to-equality.py` | Operator overloading with mixed types › Finishing `__eq__`: `NotImplemented` applies to equality too (line 1513) | may use names from earlier examples |
| `examples/40_finishing-eq-notimplemented-applies-to-equality.py` | Operator overloading with mixed types › Finishing `__eq__`: `NotImplemented` applies to equality too (line 1539) | may use names from earlier examples |
| `examples/41_reflected-comparisons-use-opposite-questions.py` | Operator overloading with mixed types › Reflected comparisons use opposite questions (line 1579) | may use names from earlier examples |
| `examples/42_matmul-and-the-operator.py` | Operator overloading with mixed types › `__matmul__` and the `@` operator (line 1642) | may use names from earlier examples |
| `examples/43_try-it-yourself.py` | Try it yourself (line 1708) | may use names from earlier examples |
