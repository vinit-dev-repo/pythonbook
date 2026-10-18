# 21.4 - Properties, Validation and Caching

The code of the chapter **21.4 - Properties, Validation and Caching** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why a bare attribute gives no control over a new value
- How `@property` and `@x.setter` run a method on read and on assignment
- How read-only, computed and deleter properties behave
- How the older `property()` call, a property factory and the accessors fit together
- How to cache a computed value and invalidate it

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `property_factory_lab.py` | Properties › A factory for related properties (line 352) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_the-problem-bare-attributes-give-no-control.py` | Properties › The problem: bare attributes give no control (line 43) | runs on its own |
| `examples/02_property-making-a-method-look-like-an-attribute.py` | Properties › `@property`: making a method look like an attribute (line 65) | may use names from earlier examples |
| `examples/03_property-making-a-method-look-like-an-attribute.py` | Properties › `@property`: making a method look like an attribute (line 87) | may use names from earlier examples |
| `examples/04_x-setter-adding-validation.py` | Properties › `@x.setter`: adding validation (line 111) | raises an error on purpose |
| `examples/05_read-only-and-computed-properties.py` | Properties › Read-only and computed properties (line 188) | may use names from earlier examples |
| `examples/06_read-only-and-computed-properties.py` | Properties › Read-only and computed properties (line 238) | may use names from earlier examples |
| `examples/07_x-deleter-running-code-when-an-attribute-is-dele.py` | Properties › `@x.deleter`: running code when an attribute is deleted (line 256) | may use names from earlier examples |
| `examples/08_the-older-property-call-form.py` | Properties › The older `property()` call form (line 302) | may use names from earlier examples |
| `examples/09_a-setter-decorator-makes-another-property.py` | Properties › A setter decorator makes another property (line 418) | may use names from earlier examples |
| `examples/10_accessors-determine-which-operations-are-availab.py` | Properties › Accessors determine which operations are available (line 486) | may use names from earlier examples |
| `examples/11_a-property-takes-priority-over-a-same-named-inst.py` | Properties › A property takes priority over a same-named instance entry (line 522) | may use names from earlier examples |
| `examples/12_deleting-backing-data-differs-from-resetting-it.py` | Properties › Deleting backing data differs from resetting it (line 538) | may use names from earlier examples |
| `examples/13_cache-a-value-until-its-input-changes.py` | Properties › Cache a value until its input changes (line 594) | may use names from earlier examples |
| `examples/14_cache-a-value-until-its-input-changes.py` | Properties › Cache a value until its input changes (line 650) | may use names from earlier examples |
| `examples/15_cache-a-value-until-its-input-changes.py` | Properties › Cache a value until its input changes (line 703) | may use names from earlier examples |
| `examples/16_exact-type-and-an-overridable-attribute.py` | Properties › Exact type and an overridable attribute (line 715) | may use names from earlier examples |
| `examples/17_try-it-yourself.py` | Try it yourself (line 767) | may use names from earlier examples |
