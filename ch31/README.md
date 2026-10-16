# 31 - Metaclasses and Metaprogramming

The code of the chapter **31 - Metaclasses and Metaprogramming** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What a metaclass is and how it relates to a class object
- How `type` acts as the default metaclass, and how a class can select another metaclass
- How to write a metaclass and when it is useful
- Which methods run when code calls `MyClass(...)`, and how class lookup differs from instance lookup
- When a class decorator or `__init_subclass__` can replace a metaclass
- How the attribute-access hooks `__getattr__`, `__getattribute__`, and `__setattr__` work, and how to avoid recursion
- Three small metaprogramming examples that you can reuse
- How display helpers and wrappers separate stored fields, representation and delegated behavior
- Why a tracing wrapper has its own state and changes the exposed type

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `type_links.py` | `type` is the default metaclass › Instance-of and subclass-of are different links (line 110) |  |
| `record_factory_lab.py` | `type` is the default metaclass › Build a mutable record class with `type` (line 180) |  |
| `namespace_policy.py` | `__prepare__` — choosing the namespace, briefly (line 525) |  |
| `class_factories.py` | A class factory can be an ordinary callable (line 580) |  |
| `metaclass_keywords.py` | Choose among class-creation tools › Apply a forwarded class keyword (line 699) |  |
| `lifecycle_model.py` | Choose among class-creation tools › Observe import, class creation and instance construction (line 758) |  |
| `lifecycle_import.py` | Choose among class-creation tools › Observe import, class creation and instance construction (line 870) |  |
| `base_paths.py` | Choose among class-creation tools › Walk every base-class path (line 935) |  |
| `meta_call_levels.py` | Classes, metaclasses, and `__call__` › Calling a metaclass has one more type level (line 1031) |  |
| `class_lookup.py` | A class reads from its bases and its metaclass (line 1125) |  |
| `deletion_hook.py` | Attribute access hooks — metaprogramming beyond creation › Deletion uses a separate hook (line 1316) |  |
| `computed_hooks.py` | Attribute access hooks — metaprogramming beyond creation › Compute a value without storing it (line 1363) |  |
| `generated_summary.py` | Three small metaprogramming applications › Generate one method from declared fields (line 1610) |  |
| `method_tools.py` | Apply a decorator to locally defined methods (line 1680) |  |
| `timed_methods.py` | Apply a decorator to locally defined methods (line 1777) |  |
| `rebuild_class.py` | Apply a decorator to locally defined methods › Rebuilding a class is not the same as updating it (line 1820) |  |
| `display_records.py` | Display and delegate a record (line 1882) |  |
| `namespace_views.py` | Display and delegate a record › Inspect three kinds of namespace (line 2025) |  |
| `inspection_tools.py` | Display and delegate a record › Inspect three kinds of namespace (line 2118) |  |
| `try_views.py` | Display and delegate a record › Inspect three kinds of namespace (line 2129) |  |
| `repr_loop.py` | Display and delegate a record › A display can call itself indirectly (line 2232) |  |
| `inspection_transfer.py` | Display and delegate a record › Transfer: shared ancestors, slots and a library class (line 2281) |  |
| `attribute_origins.py` | Display and delegate a record › Map definitions without reading their values (line 2382) |  |
| `delegate_record.py` | Display and delegate a record › A wrapper forwards only the operations it implements (line 2491) |  |
| `tracer_lab.py` | Trace a constructed target (line 2578) |  |
| `class_factory_trace.py` | Trace a constructed target › A class factory can return a tracing wrapper (line 2726) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_type-is-the-default-metaclass.py` | `type` is the default metaclass (line 77) | runs on its own |
| `examples/02_creating-a-class-without-the-class-statement.py` | `type` is the default metaclass › Creating a class WITHOUT the `class` statement (line 138) | may use names from earlier examples |
| `examples/03_new-vs-init-on-ordinary-classes-first.py` | `__new__` vs `__init__` on ordinary classes, first (line 292) | may use names from earlier examples |
| `examples/04_when-to-override-new.py` | `__new__` vs `__init__` on ordinary classes, first › When to override `__new__` (line 325) | may use names from earlier examples |
| `examples/05_inheriting-from-type-your-own-metaclass.py` | Inheriting from `type`: your own metaclass (line 359) | may use names from earlier examples |
| `examples/06_worked-example-every-class-must-define-x.py` | Inheriting from `type`: your own metaclass › Worked example: every class must define X (line 390) | may use names from earlier examples |
| `examples/07_worked-example-auto-register-every-subclass.py` | Inheriting from `type`: your own metaclass › Worked example: auto-register every subclass (line 424) | may use names from earlier examples |
| `examples/08_metaclass-keyword-and-metaclass-parameters.py` | `metaclass=` keyword and metaclass parameters (line 463) | may use names from earlier examples |
| `examples/09_prepare-choosing-the-namespace-briefly.py` | `__prepare__` — choosing the namespace, briefly (line 491) | may use names from earlier examples |
| `examples/10_init-subclass-the-modern-hook-and-the-one-to-rea.py` | Choose among class-creation tools › `__init_subclass__` — the modern hook, and the one to reach for first (line 666) | may use names from earlier examples |
| `examples/11_classes-metaclasses-and-call.py` | Classes, metaclasses, and `__call__` (line 1007) | may use names from earlier examples |
| `examples/12_singleton-via-metaclass-call.py` | Classes, metaclasses, and `__call__` › Singleton via metaclass `__call__` (line 1088) | may use names from earlier examples |
| `examples/13_getattr-the-missing-only-fallback.py` | Attribute access hooks — metaprogramming beyond creation › `__getattr__`: the missing-only fallback (line 1210) | may use names from earlier examples |
| `examples/14_getattribute-every-attribute-read.py` | Attribute access hooks — metaprogramming beyond creation › `__getattribute__`: every attribute read (line 1243) | may use names from earlier examples |
| `examples/15_setattr-the-same-trap-on-writing.py` | Attribute access hooks — metaprogramming beyond creation › `__setattr__`: the same trap, on writing (line 1278) | may use names from earlier examples |
| `examples/16_practical-application-an-attribute-access-logger.py` | Attribute access hooks — metaprogramming beyond creation › Practical application: an attribute-access logger (line 1457) | may use names from earlier examples |
| `examples/17_1-auto-repr-via-class-decorator.py` | Three small metaprogramming applications › 1. Auto-repr via class decorator (line 1504) | may use names from earlier examples |
| `examples/18_2-subclass-registry-via-init-subclass.py` | Three small metaprogramming applications › 2. Subclass registry via `__init_subclass__` (line 1539) | may use names from earlier examples |
| `examples/19_3-class-validation-via-metaclass.py` | Three small metaprogramming applications › 3. Class validation via metaclass (line 1569) | may use names from earlier examples |
| `examples/20_predict-which-fields-are-displayed.py` | Display and delegate a record › Predict which fields are displayed (line 1984) | runs on its own |
| `examples/21_a-wrapper-forwards-only-the-operations-it-implem.py` | Display and delegate a record › A wrapper forwards only the operations it implements (line 2545) | runs on its own |
| `examples/22_trace-a-constructed-target.py` | Trace a constructed target (line 2643) | runs on its own |
| `examples/23_trace-a-constructed-target.py` | Trace a constructed target (line 2661) | runs on its own |
| `examples/24_trace-a-constructed-target.py` | Trace a constructed target (line 2697) | runs on its own |
| `examples/25_try-it-yourself.py` | Try it yourself (line 2787) | may use names from earlier examples |
| `examples/26_2-find-the-problem.py` | 2. Find the problem (line 2893) | runs on its own |
| `examples/27_3-build.py` | 3. Build (line 2932) | runs on its own |
