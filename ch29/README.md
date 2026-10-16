# 29 - Descriptors

The code of this chapter of the Python tutorial, extracted byte for byte from the certified chapter. The chapter explains every line; read it there.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

- `registration_transfer.py`

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Section | Note |
|---|---|---|
| `examples/01_what-a-descriptor-is.py` | What a descriptor is | runs on its own |
| `examples/02_the-protocol-get-set-delete.py` | The protocol: `__get__`, `__set__`, `__delete__` | may use names from earlier examples |
| `examples/03_reading-through-the-class-and-deleting-a-managed.py` | Reading through the class, and deleting a managed value | runs on its own |
| `examples/04_step-1-the-naive-version.py` | Step 1 — the naive version | may use names from earlier examples |
| `examples/05_the-wrong-way-storing-on-the-descriptor-two-inst.py` | The wrong way: storing on the descriptor — two instances trample each other | may use names from earlier examples |
| `examples/06_a-better-way-a-dictionary-keyed-by-the-instance.py` | A better way: a dictionary keyed by the instance | may use names from earlier examples |
| `examples/07_the-memory-leak-and-weak-references-fixing-it.py` | The memory leak, and weak references fixing it | may use names from earlier examples |
| `examples/08_the-modern-answer-set-name.py` | The modern answer: `__set_name__` | may use names from earlier examples |
| `examples/09_attribute-lookup-the-exact-order.py` | Attribute lookup — the exact order | may use names from earlier examples |
| `examples/10_a-writer-without-a-getter-and-a-delete-only-desc.py` | A writer without a getter, and a delete-only descriptor | runs on its own |
| `examples/11_replacing-the-descriptor-on-its-owner-class.py` | Replacing the descriptor on its owner class | runs on its own |
| `examples/12_when-a-getter-raises-attributeerror.py` | When a getter raises `AttributeError` | runs on its own |
| `examples/13_why-instance-attributes-do-not-override-data-des.py` | Why instance attributes do not override data descriptors | may use names from earlier examples |
| `examples/14_property-is-a-descriptor.py` | `property` IS a descriptor | may use names from earlier examples |
| `examples/15_functions-are-descriptors-how-methods-work.py` | Functions are descriptors: how methods work | may use names from earlier examples |
| `examples/16_functions-are-descriptors-how-methods-work.py` | Functions are descriptors: how methods work | may use names from earlier examples |
| `examples/17_binding-behavior-to-one-instance.py` | Binding behavior to one instance | may use names from earlier examples |
| `examples/18_binding-behavior-to-one-instance.py` | Binding behavior to one instance | may use names from earlier examples |
| `examples/19_descriptors-and-inheritance-found-through-the-mr.py` | Descriptors and inheritance: found through the MRO | may use names from earlier examples |
| `examples/20_a-subclass-can-shadow-the-descriptor-and-lose-th.py` | A subclass can shadow the descriptor — and lose the protection | may use names from earlier examples |
| `examples/21_application-1-a-reusable-validation-family.py` | Application 1: a reusable validation family | may use names from earlier examples |
| `examples/22_continue-the-bounded-field-lab.py` | Continue the bounded-field lab | may use names from earlier examples |
| `examples/23_when-validation-also-changes-a-value.py` | When validation also changes a value | runs on its own |
| `examples/24_application-2-a-lazy-cached-attribute.py` | Application 2: a lazy (cached) attribute | may use names from earlier examples |
| `examples/25_transfer-invalidate-a-lazy-cached-value.py` | Transfer — invalidate a lazy cached value | may use names from earlier examples |
| `examples/26_a-cache-that-does-not-cause-a-leak-weakvaluedict.py` | A cache that does not cause a leak: `WeakValueDictionary` | may use names from earlier examples |
| `examples/27_try-it-yourself.py` | Try it yourself | may use names from earlier examples |
