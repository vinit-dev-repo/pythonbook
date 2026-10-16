# 21 - Classes and Objects

The code of this chapter of the Python tutorial, extracted byte for byte from the certified chapter. The chapter explains every line; read it there.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

- `circle_state.py`
- `property_factory_lab.py`

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Section | Note |
|---|---|---|
| `examples/01_defining-a-class.py` | Defining a class | runs on its own |
| `examples/02_defining-a-class.py` | Defining a class | may use names from earlier examples |
| `examples/03_defining-a-class.py` | Defining a class | may use names from earlier examples |
| `examples/04_defining-a-class.py` | Defining a class | may use names from earlier examples |
| `examples/05_init-preparing-a-new-object.py` | `__init__`: preparing a new object | may use names from earlier examples |
| `examples/06_self-explained-slowly.py` | `self`, explained slowly | may use names from earlier examples |
| `examples/07_instance-attributes.py` | Instance attributes | may use names from earlier examples |
| `examples/08_class-attributes.py` | Class attributes | may use names from earlier examples |
| `examples/09_class-attributes.py` | Class attributes | may use names from earlier examples |
| `examples/10_why-mutable-class-attributes-can-cause-problems.py` | Why mutable class attributes can cause problems | may use names from earlier examples |
| `examples/11_why-mutable-class-attributes-can-cause-problems.py` | Why mutable class attributes can cause problems | may use names from earlier examples |
| `examples/12_methods.py` | Methods | may use names from earlier examples |
| `examples/13_methods.py` | Methods | may use names from earlier examples |
| `examples/14_a-method-can-replace-an-immutable-field.py` | A method can replace an immutable field | may use names from earlier examples |
| `examples/15_a-method-can-replace-an-immutable-field.py` | A method can replace an immutable field | may use names from earlier examples |
| `examples/16_classes-are-callable.py` | Classes are callable | may use names from earlier examples |
| `examples/17_python-s-built-in-types-are-classes-too.py` | Python's built-in types are classes too | may use names from earlier examples |
| `examples/18_python-s-built-in-types-are-classes-too.py` | Python's built-in types are classes too | may use names from earlier examples |
| `examples/19_adding-attributes-at-runtime.py` | Adding attributes at runtime | may use names from earlier examples |
| `examples/20_adding-attributes-at-runtime.py` | Adding attributes at runtime | may use names from earlier examples |
| `examples/21_adding-attributes-at-runtime.py` | Adding attributes at runtime | may use names from earlier examples |
| `examples/22_adding-attributes-at-runtime.py` | Adding attributes at runtime | may use names from earlier examples |
| `examples/23_adding-attributes-at-runtime.py` | Adding attributes at runtime | may use names from earlier examples |
| `examples/24_adding-attributes-at-runtime.py` | Adding attributes at runtime | may use names from earlier examples |
| `examples/25_callable-attributes-and-function-attributes.py` | Callable attributes and function attributes | may use names from earlier examples |
| `examples/26_callable-attributes-and-function-attributes.py` | Callable attributes and function attributes | may use names from earlier examples |
| `examples/27_the-problem-bare-attributes-give-no-control.py` | The problem: bare attributes give no control | may use names from earlier examples |
| `examples/28_property-making-a-method-look-like-an-attribute.py` | `@property`: making a method look like an attribute | may use names from earlier examples |
| `examples/29_property-making-a-method-look-like-an-attribute.py` | `@property`: making a method look like an attribute | may use names from earlier examples |
| `examples/30_x-setter-adding-validation.py` | `@x.setter`: adding validation | raises an error on purpose |
| `examples/31_read-only-and-computed-properties.py` | Read-only and computed properties | may use names from earlier examples |
| `examples/32_read-only-and-computed-properties.py` | Read-only and computed properties | may use names from earlier examples |
| `examples/33_x-deleter-running-code-when-an-attribute-is-dele.py` | `@x.deleter`: running code when an attribute is deleted | may use names from earlier examples |
| `examples/34_the-older-property-call-form.py` | The older `property()` call form | may use names from earlier examples |
| `examples/35_a-setter-decorator-makes-another-property.py` | A setter decorator makes another property | may use names from earlier examples |
| `examples/36_accessors-determine-which-operations-are-availab.py` | Accessors determine which operations are available | may use names from earlier examples |
| `examples/37_a-property-takes-priority-over-a-same-named-inst.py` | A property takes priority over a same-named instance entry | may use names from earlier examples |
| `examples/38_deleting-backing-data-differs-from-resetting-it.py` | Deleting backing data differs from resetting it | may use names from earlier examples |
| `examples/39_cache-a-value-until-its-input-changes.py` | Cache a value until its input changes | may use names from earlier examples |
| `examples/40_cache-a-value-until-its-input-changes.py` | Cache a value until its input changes | may use names from earlier examples |
| `examples/41_cache-a-value-until-its-input-changes.py` | Cache a value until its input changes | may use names from earlier examples |
| `examples/42_exact-type-and-an-overridable-attribute.py` | Exact type and an overridable attribute | may use names from earlier examples |
| `examples/43_classmethod-alternative-constructors.py` | `@classmethod`: alternative constructors | may use names from earlier examples |
| `examples/44_classmethod-alternative-constructors.py` | `@classmethod`: alternative constructors | may use names from earlier examples |
| `examples/45_staticmethod-a-helper-that-just-belongs-with-the.py` | `@staticmethod`: a helper that just belongs with the class | may use names from earlier examples |
| `examples/46_staticmethod-a-helper-that-just-belongs-with-the.py` | `@staticmethod`: a helper that just belongs with the class | may use names from earlier examples |
| `examples/47_follow-the-receiver-through-an-instance-call.py` | Follow the receiver through an instance call | may use names from earlier examples |
| `examples/48_the-class-body-runs-when-execution-reaches-it.py` | The class body runs when execution reaches it | runs on its own |
| `examples/49_repeating-a-method-name-replaces-its-earlier-def.py` | Repeating a method name replaces its earlier definition | runs on its own |
| `examples/50_class-bodies-are-not-enclosing-scopes.py` | Class bodies are not enclosing scopes | raises an error on purpose |
| `examples/51_class-bodies-are-not-enclosing-scopes.py` | Class bodies are not enclosing scopes | may use names from earlier examples |
| `examples/52_class-bodies-are-not-enclosing-scopes.py` | Class bodies are not enclosing scopes | raises an error on purpose |
| `examples/53_class-bodies-are-not-enclosing-scopes.py` | Class bodies are not enclosing scopes | may use names from earlier examples |
| `examples/54_a-global-or-enclosing-function-can-still-supply.py` | A global or enclosing function can still supply a name | runs on its own |
| `examples/55_a-global-or-enclosing-function-can-still-supply.py` | A global or enclosing function can still supply a name | may use names from earlier examples |
| `examples/56_try-it-yourself.py` | Try it yourself | may use names from earlier examples |
