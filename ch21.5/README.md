# 21.5 - Class Methods, Static Methods and the Class Body

The code of the chapter **21.5 - Class Methods, Static Methods and the Class Body** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How `@classmethod` and `cls` build an alternative constructor
- How `@staticmethod` groups a helper with the class
- Which receiver a plain, class and static method each gets
- When Python runs the class body, and what a repeated method name does
- Why a method cannot read a class attribute by its bare name

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_classmethod-alternative-constructors.py` | Class methods and static methods › `@classmethod`: alternative constructors (line 43) | runs on its own |
| `examples/02_classmethod-alternative-constructors.py` | Class methods and static methods › `@classmethod`: alternative constructors (line 94) | may use names from earlier examples |
| `examples/03_staticmethod-a-helper-that-just-belongs-with-the.py` | Class methods and static methods › `@staticmethod`: a helper that just belongs with the class (line 112) | may use names from earlier examples |
| `examples/04_staticmethod-a-helper-that-just-belongs-with-the.py` | Class methods and static methods › `@staticmethod`: a helper that just belongs with the class (line 123) | may use names from earlier examples |
| `examples/05_follow-the-receiver-through-an-instance-call.py` | Class methods and static methods › Follow the receiver through an instance call (line 157) | may use names from earlier examples |
| `examples/06_the-class-body-runs-when-execution-reaches-it.py` | The class body runs when execution reaches it (line 261) | runs on its own |
| `examples/07_repeating-a-method-name-replaces-its-earlier-def.py` | The class body runs when execution reaches it › Repeating a method name replaces its earlier definition (line 293) | runs on its own |
| `examples/08_class-bodies-are-not-enclosing-scopes.py` | The class body runs when execution reaches it › Class bodies are not enclosing scopes (line 340) | raises an error on purpose |
| `examples/09_class-bodies-are-not-enclosing-scopes.py` | The class body runs when execution reaches it › Class bodies are not enclosing scopes (line 364) | may use names from earlier examples |
| `examples/10_class-bodies-are-not-enclosing-scopes.py` | The class body runs when execution reaches it › Class bodies are not enclosing scopes (line 384) | raises an error on purpose |
| `examples/11_class-bodies-are-not-enclosing-scopes.py` | The class body runs when execution reaches it › Class bodies are not enclosing scopes (line 407) | may use names from earlier examples |
| `examples/12_a-global-or-enclosing-function-can-still-supply.py` | The class body runs when execution reaches it › A global or enclosing function can still supply a name (line 430) | runs on its own |
| `examples/13_a-global-or-enclosing-function-can-still-supply.py` | The class body runs when execution reaches it › A global or enclosing function can still supply a name (line 469) | may use names from earlier examples |
| `examples/14_try-it-yourself.py` | Try it yourself (line 520) | may use names from earlier examples |
