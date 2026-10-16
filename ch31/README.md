# 31 - Metaclasses and Metaprogramming

The code of this chapter of the Python tutorial, extracted byte for byte from the certified chapter. The chapter explains every line; read it there.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

- `attribute_origins.py`
- `base_paths.py`
- `class_factories.py`
- `class_factory_trace.py`
- `class_lookup.py`
- `computed_hooks.py`
- `delegate_record.py`
- `deletion_hook.py`
- `display_records.py`
- `generated_summary.py`
- `inspection_tools.py`
- `inspection_transfer.py`
- `lifecycle_import.py`
- `lifecycle_model.py`
- `meta_call_levels.py`
- `metaclass_keywords.py`
- `method_tools.py`
- `namespace_policy.py`
- `namespace_views.py`
- `rebuild_class.py`
- `record_factory_lab.py`
- `repr_loop.py`
- `timed_methods.py`
- `tracer_lab.py`
- `try_views.py`
- `type_links.py`

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Section | Note |
|---|---|---|
| `examples/01_type-is-the-default-metaclass.py` | `type` is the default metaclass | runs on its own |
| `examples/02_creating-a-class-without-the-class-statement.py` | Creating a class WITHOUT the `class` statement | may use names from earlier examples |
| `examples/03_new-vs-init-on-ordinary-classes-first.py` | `__new__` vs `__init__` on ordinary classes, first | may use names from earlier examples |
| `examples/04_when-to-override-new.py` | When to override `__new__` | may use names from earlier examples |
| `examples/05_inheriting-from-type-your-own-metaclass.py` | Inheriting from `type`: your own metaclass | may use names from earlier examples |
| `examples/06_worked-example-every-class-must-define-x.py` | Worked example: every class must define X | may use names from earlier examples |
| `examples/07_worked-example-auto-register-every-subclass.py` | Worked example: auto-register every subclass | may use names from earlier examples |
| `examples/08_metaclass-keyword-and-metaclass-parameters.py` | `metaclass=` keyword and metaclass parameters | may use names from earlier examples |
| `examples/09_prepare-choosing-the-namespace-briefly.py` | `__prepare__` — choosing the namespace, briefly | may use names from earlier examples |
| `examples/10_init-subclass-the-modern-hook-and-the-one-to-rea.py` | `__init_subclass__` — the modern hook, and the one to reach for first | may use names from earlier examples |
| `examples/11_classes-metaclasses-and-call.py` | Classes, metaclasses, and `__call__` | may use names from earlier examples |
| `examples/12_singleton-via-metaclass-call.py` | Singleton via metaclass `__call__` | may use names from earlier examples |
| `examples/13_getattr-the-missing-only-fallback.py` | `__getattr__`: the missing-only fallback | may use names from earlier examples |
| `examples/14_getattribute-every-attribute-read.py` | `__getattribute__`: every attribute read | may use names from earlier examples |
| `examples/15_setattr-the-same-trap-on-writing.py` | `__setattr__`: the same trap, on writing | may use names from earlier examples |
| `examples/16_practical-application-an-attribute-access-logger.py` | Practical application: an attribute-access logger | may use names from earlier examples |
| `examples/17_1-auto-repr-via-class-decorator.py` | 1. Auto-repr via class decorator | may use names from earlier examples |
| `examples/18_2-subclass-registry-via-init-subclass.py` | 2. Subclass registry via `__init_subclass__` | may use names from earlier examples |
| `examples/19_3-class-validation-via-metaclass.py` | 3. Class validation via metaclass | may use names from earlier examples |
| `examples/20_predict-which-fields-are-displayed.py` | Predict which fields are displayed | runs on its own |
| `examples/21_a-wrapper-forwards-only-the-operations-it-implem.py` | A wrapper forwards only the operations it implements | runs on its own |
| `examples/22_trace-a-constructed-target.py` | Trace a constructed target | runs on its own |
| `examples/23_trace-a-constructed-target.py` | Trace a constructed target | runs on its own |
| `examples/24_trace-a-constructed-target.py` | Trace a constructed target | runs on its own |
| `examples/25_try-it-yourself.py` | Try it yourself | may use names from earlier examples |
| `examples/26_2-find-the-problem.py` | 2. Find the problem | runs on its own |
| `examples/27_3-build.py` | 3. Build | runs on its own |
