# 22 - Special Dunder Methods

The code of this chapter of the Python tutorial, extracted byte for byte from the certified chapter. The chapter explains every line; read it there.

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Section | Note |
|---|---|---|
| `examples/01_what-dunder-methods-are.py` | What dunder methods are | runs on its own |
| `examples/02_direct-lookup-and-implicit-lookup.py` | Direct lookup and implicit lookup | may use names from earlier examples |
| `examples/03_str-vs-repr.py` | `__str__` vs `__repr__` | may use names from earlier examples |
| `examples/04_display-does-not-define-a-reconstruction-format.py` | Display does not define a reconstruction format | may use names from earlier examples |
| `examples/05_bytes-a-binary-representation.py` | `__bytes__`: a binary representation | may use names from earlier examples |
| `examples/06_add-sub-mul.py` | `__add__`, `__sub__`, `__mul__` | may use names from earlier examples |
| `examples/07_eq-and-equality.py` | `__eq__` and equality | may use names from earlier examples |
| `examples/08_eq-and-equality.py` | `__eq__` and equality | may use names from earlier examples |
| `examples/09_the-other-comparisons.py` | The other comparisons: `<`, `<=`, `>`, `>=` | may use names from earlier examples |
| `examples/10_defining-eq-makes-instances-unhashable-by-defaul.py` | Defining `__eq__` makes instances unhashable by default | may use names from earlier examples |
| `examples/11_defining-eq-makes-instances-unhashable-by-defaul.py` | Defining `__eq__` makes instances unhashable by default | may use names from earlier examples |
| `examples/12_defining-eq-makes-instances-unhashable-by-defaul.py` | Defining `__eq__` makes instances unhashable by default | may use names from earlier examples |
| `examples/13_what-breaks-if-the-hash-disagrees-with-equality.py` | What breaks if the hash disagrees with equality | may use names from earlier examples |
| `examples/14_a-collision-is-not-an-equality-claim.py` | A collision is not an equality claim | may use names from earlier examples |
| `examples/15_bool-and-len.py` | `__bool__` and `__len__` | may use names from earlier examples |
| `examples/16_bool-and-len.py` | `__bool__` and `__len__` | may use names from earlier examples |
| `examples/17_default-truth-and-method-requirements.py` | Default truth and method requirements | may use names from earlier examples |
| `examples/18_call-objects-you-can-call-like-a-function.py` | `__call__`: objects you can call like a function | may use names from earlier examples |
| `examples/19_format.py` | `__format__` | may use names from earlier examples |
| `examples/20_forwarding-a-format-to-a-stored-value.py` | Forwarding a format to a stored value | may use names from earlier examples |
| `examples/21_index-an-exact-integer-for-python-s-integer-only.py` | `__index__`: an exact integer for Python's integer-only operations | may use names from earlier examples |
| `examples/22_exact-indices-differ-from-numeric-conversion.py` | Exact indices differ from numeric conversion | may use names from earlier examples |
| `examples/23_how-python-picks-which-method-runs-for-a-b.py` | How Python picks which method runs for `a + b` | may use names from earlier examples |
| `examples/24_notimplemented-is-not-notimplementederror.py` | `NotImplemented` is not `NotImplementedError` | may use names from earlier examples |
| `examples/25_refusal-absence-and-exceptions.py` | Refusal, absence, and exceptions | may use names from earlier examples |
| `examples/26_reflected-operators-making-the-right-hand-side-w.py` | Reflected operators: making the right-hand side work too | may use names from earlier examples |
| `examples/27_reflected-operators-making-the-right-hand-side-w.py` | Reflected operators: making the right-hand side work too | may use names from earlier examples |
| `examples/28_reflected-operators-making-the-right-hand-side-w.py` | Reflected operators: making the right-hand side work too | may use names from earlier examples |
| `examples/29_reflected-operators-making-the-right-hand-side-w.py` | Reflected operators: making the right-hand side work too | may use names from earlier examples |
| `examples/30_returning-a-wrapper-without-nesting-wrappers.py` | Returning a wrapper without nesting wrappers | may use names from earlier examples |
| `examples/31_subtraction-and-division-order-matters.py` | Subtraction and division: order matters | may use names from earlier examples |
| `examples/32_unary-operators-neg-pos-abs-invert.py` | Unary operators: `__neg__`, `__pos__`, `__abs__`, `__invert__` | may use names from earlier examples |
| `examples/33_unary-plus-can-apply-a-type-specific-rule.py` | Unary plus can apply a type-specific rule | may use names from earlier examples |
| `examples/34_unary-plus-can-apply-a-type-specific-rule.py` | Unary plus can apply a type-specific rule | may use names from earlier examples |
| `examples/35_in-place-operators-iadd-and-friends.py` | In-place operators: `__iadd__` and friends | may use names from earlier examples |
| `examples/36_in-place-operators-iadd-and-friends.py` | In-place operators: `__iadd__` and friends | may use names from earlier examples |
| `examples/37_following-aliases-through-augmented-assignment.py` | Following aliases through augmented assignment | may use names from earlier examples |
| `examples/38_finishing-eq-notimplemented-applies-to-equality.py` | Finishing `__eq__`: `NotImplemented` applies to equality too | may use names from earlier examples |
| `examples/39_finishing-eq-notimplemented-applies-to-equality.py` | Finishing `__eq__`: `NotImplemented` applies to equality too | may use names from earlier examples |
| `examples/40_finishing-eq-notimplemented-applies-to-equality.py` | Finishing `__eq__`: `NotImplemented` applies to equality too | may use names from earlier examples |
| `examples/41_reflected-comparisons-use-opposite-questions.py` | Reflected comparisons use opposite questions | may use names from earlier examples |
| `examples/42_matmul-and-the-operator.py` | `__matmul__` and the `@` operator | may use names from earlier examples |
| `examples/43_try-it-yourself.py` | Try it yourself | may use names from earlier examples |
