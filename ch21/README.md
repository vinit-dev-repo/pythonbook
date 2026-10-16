# 21 - Classes and Objects

The code of the chapter **21 - Classes and Objects** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why classes exist: keeping data and the functions that work on it together
- How to define a class and create objects from it
- How `__init__` and `self` set up a new object automatically
- The difference between instance attributes and class attributes, and why mutable class attributes can cause problems
- How to control access to an attribute with `@property`
- Class methods and static methods, and when to use each
- How to build a `BankAccount` class one step at a time

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `circle_state.py` | A method can replace an immutable field (line 477) |  |
| `property_factory_lab.py` | A factory for related properties (line 1254) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_defining-a-class.py` | Defining a class (line 82) | runs on its own |
| `examples/02_defining-a-class.py` | Defining a class (line 99) | may use names from earlier examples |
| `examples/03_defining-a-class.py` | Defining a class (line 119) | may use names from earlier examples |
| `examples/04_defining-a-class.py` | Defining a class (line 135) | may use names from earlier examples |
| `examples/05_init-preparing-a-new-object.py` | `__init__`: preparing a new object (line 163) | may use names from earlier examples |
| `examples/06_self-explained-slowly.py` | `self`, explained slowly (line 212) | may use names from earlier examples |
| `examples/07_instance-attributes.py` | Instance attributes (line 238) | may use names from earlier examples |
| `examples/08_class-attributes.py` | Class attributes (line 268) | may use names from earlier examples |
| `examples/09_class-attributes.py` | Class attributes (line 307) | may use names from earlier examples |
| `examples/10_why-mutable-class-attributes-can-cause-problems.py` | Why mutable class attributes can cause problems (line 330) | may use names from earlier examples |
| `examples/11_why-mutable-class-attributes-can-cause-problems.py` | Why mutable class attributes can cause problems (line 353) | may use names from earlier examples |
| `examples/12_methods.py` | Methods (line 401) | may use names from earlier examples |
| `examples/13_methods.py` | Methods (line 440) | may use names from earlier examples |
| `examples/14_a-method-can-replace-an-immutable-field.py` | A method can replace an immutable field (line 546) | may use names from earlier examples |
| `examples/15_a-method-can-replace-an-immutable-field.py` | A method can replace an immutable field (line 593) | may use names from earlier examples |
| `examples/16_classes-are-callable.py` | Classes are callable (line 634) | may use names from earlier examples |
| `examples/17_python-s-built-in-types-are-classes-too.py` | Python's built-in types are classes too (line 652) | may use names from earlier examples |
| `examples/18_python-s-built-in-types-are-classes-too.py` | Python's built-in types are classes too (line 686) | may use names from earlier examples |
| `examples/19_adding-attributes-at-runtime.py` | Adding attributes at runtime (line 712) | may use names from earlier examples |
| `examples/20_adding-attributes-at-runtime.py` | Adding attributes at runtime (line 725) | may use names from earlier examples |
| `examples/21_adding-attributes-at-runtime.py` | Adding attributes at runtime (line 741) | may use names from earlier examples |
| `examples/22_adding-attributes-at-runtime.py` | Adding attributes at runtime (line 764) | may use names from earlier examples |
| `examples/23_adding-attributes-at-runtime.py` | Adding attributes at runtime (line 788) | may use names from earlier examples |
| `examples/24_adding-attributes-at-runtime.py` | Adding attributes at runtime (line 823) | may use names from earlier examples |
| `examples/25_callable-attributes-and-function-attributes.py` | Callable attributes and function attributes (line 888) | may use names from earlier examples |
| `examples/26_callable-attributes-and-function-attributes.py` | Callable attributes and function attributes (line 910) | may use names from earlier examples |
| `examples/27_the-problem-bare-attributes-give-no-control.py` | The problem: bare attributes give no control (line 940) | may use names from earlier examples |
| `examples/28_property-making-a-method-look-like-an-attribute.py` | `@property`: making a method look like an attribute (line 957) | may use names from earlier examples |
| `examples/29_property-making-a-method-look-like-an-attribute.py` | `@property`: making a method look like an attribute (line 980) | may use names from earlier examples |
| `examples/30_x-setter-adding-validation.py` | `@x.setter`: adding validation (line 1005) | raises an error on purpose |
| `examples/31_read-only-and-computed-properties.py` | Read-only and computed properties (line 1085) | may use names from earlier examples |
| `examples/32_read-only-and-computed-properties.py` | Read-only and computed properties (line 1134) | may use names from earlier examples |
| `examples/33_x-deleter-running-code-when-an-attribute-is-dele.py` | `@x.deleter`: running code when an attribute is deleted (line 1154) | may use names from earlier examples |
| `examples/34_the-older-property-call-form.py` | The older `property()` call form (line 1202) | may use names from earlier examples |
| `examples/35_a-setter-decorator-makes-another-property.py` | A setter decorator makes another property (line 1322) | may use names from earlier examples |
| `examples/36_accessors-determine-which-operations-are-availab.py` | Accessors determine which operations are available (line 1393) | may use names from earlier examples |
| `examples/37_a-property-takes-priority-over-a-same-named-inst.py` | A property takes priority over a same-named instance entry (line 1431) | may use names from earlier examples |
| `examples/38_deleting-backing-data-differs-from-resetting-it.py` | Deleting backing data differs from resetting it (line 1449) | may use names from earlier examples |
| `examples/39_cache-a-value-until-its-input-changes.py` | Cache a value until its input changes (line 1505) | may use names from earlier examples |
| `examples/40_cache-a-value-until-its-input-changes.py` | Cache a value until its input changes (line 1560) | may use names from earlier examples |
| `examples/41_cache-a-value-until-its-input-changes.py` | Cache a value until its input changes (line 1614) | may use names from earlier examples |
| `examples/42_exact-type-and-an-overridable-attribute.py` | Exact type and an overridable attribute (line 1630) | may use names from earlier examples |
| `examples/43_classmethod-alternative-constructors.py` | `@classmethod`: alternative constructors (line 1664) | may use names from earlier examples |
| `examples/44_classmethod-alternative-constructors.py` | `@classmethod`: alternative constructors (line 1715) | may use names from earlier examples |
| `examples/45_staticmethod-a-helper-that-just-belongs-with-the.py` | `@staticmethod`: a helper that just belongs with the class (line 1735) | may use names from earlier examples |
| `examples/46_staticmethod-a-helper-that-just-belongs-with-the.py` | `@staticmethod`: a helper that just belongs with the class (line 1746) | may use names from earlier examples |
| `examples/47_follow-the-receiver-through-an-instance-call.py` | Follow the receiver through an instance call (line 1783) | may use names from earlier examples |
| `examples/48_the-class-body-runs-when-execution-reaches-it.py` | The class body runs when execution reaches it (line 1882) | runs on its own |
| `examples/49_repeating-a-method-name-replaces-its-earlier-def.py` | Repeating a method name replaces its earlier definition (line 1916) | runs on its own |
| `examples/50_class-bodies-are-not-enclosing-scopes.py` | Class bodies are not enclosing scopes (line 1964) | raises an error on purpose |
| `examples/51_class-bodies-are-not-enclosing-scopes.py` | Class bodies are not enclosing scopes (line 1989) | may use names from earlier examples |
| `examples/52_class-bodies-are-not-enclosing-scopes.py` | Class bodies are not enclosing scopes (line 2009) | raises an error on purpose |
| `examples/53_class-bodies-are-not-enclosing-scopes.py` | Class bodies are not enclosing scopes (line 2033) | may use names from earlier examples |
| `examples/54_a-global-or-enclosing-function-can-still-supply.py` | A global or enclosing function can still supply a name (line 2057) | runs on its own |
| `examples/55_a-global-or-enclosing-function-can-still-supply.py` | A global or enclosing function can still supply a name (line 2096) | may use names from earlier examples |
| `examples/56_try-it-yourself.py` | Try it yourself (line 2148) | may use names from earlier examples |
