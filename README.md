# pythonbook

The code of the **Python tutorial** (the LearnAIConcepts programme), one folder per chapter, extracted byte for byte from each certified chapter. Nothing here is meant to be read on its own: read the chapter, which explains every line. Every example was run on **Python 3.15.0** by the tutorial's code gate.

Each folder holds the files the chapter asks you to save, an `examples/` folder with every other Python block in reading order, and a `commands/` folder with its terminal commands. The folder's `README.md` lists them all (`ABOUT.md` where the chapter's project has a README of its own). Chapter 56 has no code and no folder.

## 01 - Orientation

| Folder | Chapter | What it teaches | Saved files | Examples | Commands |
|---|---|---|---|---|---|
| [`ch01.2`](ch01.2/) | How Python Runs Your Code | What an interpreter does, in one useful sentence; What a greeting program looks like before you set anything… | 0 | 1 | 0 |
| [`ch02.1`](ch02.1/) | Getting Ready to Run Python | How to check whether Python is already installed, and how to install it on Windows, Mac and Linux if it is… | 0 | 0 | 3 |
| [`ch02.2`](ch02.2/) | Running Your First Python Program | How to create a folder and file in an editor, then save, run, edit, save, and rerun that file; How to read… | 2 | 6 | 0 |
| [`ch02.3`](ch02.3/) | Environments, Packages and Your First Project | What a virtual environment is, why you need one, and how to make and use one; How to install packages with… | 1 | 0 | 5 |
| [`ch02.4`](ch02.4/) | Choosing Your Python Tools | The three jobs of a setup, and which tool does which; How the same small program runs with Poetry, uv and… | 2 | 0 | 4 |
| [`ch03.1`](ch03.1/) | Reading Your Python Version | How Python's version numbers work; How to check which version you are running, in a terminal and in code;… | 0 | 2 | 0 |
| [`ch03.2`](ch03.2/) | Python 3.0 to 3.9 - What Changed | Why knowing your Python version actually matters; How to read an old migration recipe safely; What changed… | 0 | 24 | 0 |
| [`ch03.3`](ch03.3/) | Python 3.10 to 3.15 - What Changed | What changed in each release from 3.10 to 3.15; What Python 3.15, this tutorial's release, adds | 0 | 16 | 0 |
| [`ch03a`](ch03a/) | Checkpoint - Orientation | You have finished the orientation and first-run path. Try these before you begin the next stage, Language… | 0 | 2 | 0 |

## 02 - Language and first tools

| Folder | Chapter | What it teaches | Saved files | Examples | Commands |
|---|---|---|---|---|---|
| [`ch04.1`](ch04.1/) | Values, Types and Variables | The basic kinds of data Python works with: numbers, text, and true/false values; That *everything* in Python… | 0 | 9 | 0 |
| [`ch04.2`](ch04.2/) | Arithmetic and Assignment Shortcuts | The arithmetic operators, including the two "strange" ones: `//` and `%`; The order Python does maths in… | 0 | 12 | 0 |
| [`ch04.3`](ch04.3/) | Comparisons, Printing and Boolean Operators | How to compare values, and how to chain comparisons; How `print` separates and ends the values it shows; How… | 0 | 9 | 0 |
| [`ch04.4`](ch04.4/) | Bitwise Operators and Flags | What bits are, and how to write a number in binary; The bitwise operators `&`, `\|`, `^`, `~`, `<<` and… | 0 | 4 | 0 |
| [`ch05.1`](ch05.1/) | Control Flow, Indentation and Decisions | What "control flow" means, and why a program needs it; Why indentation matters in Python (it is not just… | 0 | 9 | 0 |
| [`ch05.2`](ch05.2/) | Repeating Work with range, for and while | `range()`, and how `for` loops walk through things; `while` loops, and the different ways a loop can end | 0 | 9 | 0 |
| [`ch05.3`](ch05.3/) | Leaving, Skipping and Finishing Loops | `break`, `continue`, and the loop `else` clause (this one confuses everyone at first); What `pass` does, and… | 0 | 10 | 0 |
| [`ch05.4`](ch05.4/) | Infinite Loops, Choosing a Loop and Worked Examples | How to escape an infinite loop; When to reach for `for` and when to reach for `while`; A small worked… | 0 | 4 | 0 |
| [`ch06.1`](ch06.1/) | Sequences and Lists | What a **sequence** is, and the three you'll use daily: `list`s, `tuple`s, `string`s; Lists: creating,… | 0 | 12 | 0 |
| [`ch06.2`](ch06.2/) | Tuples and Slicing | Tuples: what "immutable" means, and when a tuple beats a list; Slicing: selecting items with… | 0 | 8 | 0 |
| [`ch06.3`](ch06.3/) | Copying and Unpacking Sequences | Why `b = a` does not copy a list, and the three ways to actually copy one; Unpacking: pulling values out of… | 0 | 12 | 0 |
| [`ch06.4`](ch06.4/) | Strings in Depth | Strings in depth: quoting, escapes and methods; Why a string never changes, and how to build new text from… | 0 | 16 | 0 |
| [`ch06.5`](ch06.5/) | f-strings and Unicode | f-strings: putting values and formats inside text; Unicode characters: why emoji work | 0 | 8 | 0 |
| [`ch07.1`](ch07.1/) | Dictionary Basics | What a dictionary is, and why it is called an **associative array**; How to create, read, add, update and… | 0 | 11 | 0 |
| [`ch07.2`](ch07.2/) | Hashable Keys and How Lookup Works | Why dictionary keys must be **hashable**, in plain words; How a dictionary turns a hash into a slot, and… | 0 | 8 | 0 |
| [`ch07.3`](ch07.3/) | Looping, Nesting and Counting with Dictionaries | How to loop over a dictionary's keys, values, and key-value pairs; Why `in` checks keys, and how to check… | 0 | 9 | 0 |
| [`ch07.4`](ch07.4/) | Sets and Choosing a Collection | What a set is, how it differs from a list, and the `{}` empty-set trap; Set operations: union, intersection,… | 0 | 9 | 0 |
| [`ch08.1`](ch08.1/) | List Comprehensions | The idea behind a comprehension: turning a build-a-list loop into one readable line; The exact anatomy of a… | 0 | 21 | 0 |
| [`ch08.2`](ch08.2/) | Dict and Set Comprehensions and the Walrus | Dict comprehensions, including inverting a dictionary and building one with `zip()`; Set comprehensions,… | 0 | 9 | 0 |
| [`ch08.3`](ch08.3/) | When Not to Use One, Generators and Practice | When NOT to use a comprehension; How a generator expression produces items on demand and is consumed once;… | 0 | 5 | 0 |
| [`ch09.1`](ch09.1/) | Defining, Calling and Returning | What a function is, and why reusing code matters; Defining a function with `def`, calling it, and what… | 0 | 10 | 0 |
| [`ch09.2`](ch09.2/) | Positional, Keyword and Default Arguments | Positional arguments, keyword arguments, and default values; The mutable default argument trap, and how to… | 0 | 11 | 0 |
| [`ch09.3`](ch09.3/) | Collecting and Unpacking Arguments | `*args` and `**kwargs`, which collect extra arguments; Unpacking a list or a dictionary into a call;… | 0 | 11 | 0 |
| [`ch09.4`](ch09.4/) | Docstrings, dir and Type Annotations | Docstrings: how to describe a function and read it back with `help()`; `dir()`: how to list an object's… | 0 | 8 | 0 |
| [`ch09.5`](ch09.5/) | Lambdas, map, filter and Built-in Helpers | Lambdas: how to write a short nameless function, and when `def` is better; `map()` and `filter()`, and how… | 0 | 14 | 0 |
| [`ch10.1`](ch10.1/) | What Goes Wrong and How to Read a Traceback | The three different ways a program can go wrong, and how to tell them apart; What an exception is, and when… | 0 | 14 | 0 |
| [`ch10.2`](ch10.2/) | Catching Exceptions with try and except | How to catch errors with `try`/`except`, and why a bare `except:` is dangerous; `else` and `finally`, the… | 1 | 8 | 0 |
| [`ch10.3`](ch10.3/) | Raising, Asserting and Inspecting Exceptions | How to raise your own exceptions, and re-raise the same one; `assert`, and why it can be switched off; How… | 3 | 5 | 0 |
| [`ch10.4`](ch10.4/) | Nested Loops, When to Catch and EAFP | How to leave several nested loops at once with a custom exception; When to catch an exception, and when to… | 1 | 4 | 0 |
| [`ch11.1`](ch11.1/) | Modules, the Standard Library and Packages | What a module is, and the different ways to `import` one; What Python's standard library gives you for free;… | 6 | 4 | 0 |
| [`ch11.2`](ch11.2/) | Working with Text Files | How to open, read and write text files safely with `with`; The difference between `"w"` and `"a"`, and why… | 0 | 9 | 0 |
| [`ch11.3`](ch11.3/) | File Paths and pathlib | The difference between an absolute and a relative file path; The modern way to work with paths: `pathlib`;… | 2 | 4 | 0 |
| [`ch12.1`](ch12.1/) | Clocks, Dates and Time Zones | How `time` measures elapsed time and pauses a program; How to forward a call through a timing helper without… | 0 | 10 | 0 |
| [`ch12.2`](ch12.2/) | CSV Files, Random Numbers and timeit | How to read and write spreadsheet-style files with `csv`; How `random` draws numbers and choices, and why a… | 0 | 11 | 0 |
| [`ch12.3`](ch12.3/) | math, bisect, array and deque | How to use `math` for square roots, rounding, `pi` and infinity; How `bisect` finds a position in a sorted… | 4 | 4 | 0 |
| [`ch12.4`](ch12.4/) | Statistics and Exact Decimals | `statistics`: mean, median, mode and spread, without doing the sums yourself; `decimal`: exact decimal… | 0 | 5 | 0 |
| [`ch12.5`](ch12.5/) | Annotations, t-strings and Text Formats | `annotationlib`: when annotations are evaluated and how that differs from type checking; Template strings:… | 0 | 17 | 0 |
| [`ch12.6`](ch12.6/) | Reading a Library's Exact Contract | How `delimiter`, `quotechar` and `skipinitialspace` change what a CSV reader returns; How a model's… | 0 | 3 | 0 |
| [`ch13.1`](ch13.1/) | Matching with the re Module | How Python's `re` API applies the pattern language from the shared Regular Expressions module; How to search… | 0 | 7 | 0 |
| [`ch13.2`](ch13.2/) | Groups, Replacing and Splitting | How Python spells and reads named groups; How to find-and-replace with `re.sub`, including captured groups;… | 0 | 5 | 0 |
| [`ch13.3`](ch13.3/) | Flags, Compiling and Where to Practise | The useful flags: `IGNORECASE`, `MULTILINE`, `DOTALL`, `VERBOSE`; When to compile a reusable `Pattern`… | 0 | 5 | 0 |
| [`ch14.1`](ch14.1/) | Characters, Bytes and Encodings | What a character really is, and the difference between a **code point** and a **byte**; The `bytes` and… | 1 | 8 | 0 |
| [`ch14.2`](ch14.2/) | Encoding Errors, Source Files and Evidence | What `UnicodeEncodeError` and `UnicodeDecodeError` each mean; How the `errors=` handlers decide what happens… | 1 | 9 | 0 |
| [`ch14.3`](ch14.3/) | The Unicode Sandwich, Files and Byte Order Marks | The Unicode sandwich: decode input, work in `str`, encode output; How to open text files with `encoding=`,… | 2 | 6 | 1 |
| [`ch14.4`](ch14.4/) | Normalisation, str and bytes APIs, Case Folding and Lookup | Why two strings that look the same can compare unequal, and how normalisation fixes it; Which… | 0 | 9 | 0 |
| [`ch14.5`](ch14.5/) | memoryview, Packed Records and Sorting Text | How a `memoryview` reads and changes existing bytes without copying them; How to cast a view, make it… | 2 | 8 | 0 |
| [`ch14a`](ch14a/) | Checkpoint - Language foundations | You have practised the basic language and text tools. Later lessons use these ideas. Spend about half an… | 0 | 3 | 0 |
| [`ch15.1`](ch15.1/) | Names, Types and Rebinding | How to trace names and the objects they refer to without guessing about memory addresses; That the type… | 0 | 5 | 0 |
| [`ch15.2`](ch15.2/) | Mutability, Aliases and Repeated Rows | Which objects can change in place, and which can only give a new result; How aliasing and shallow copies… | 0 | 9 | 0 |
| [`ch15.3`](ch15.3/) | Function Arguments, is and == | How a function's parameter shares the caller's object, and what rebinding a parameter does; How to choose… | 0 | 5 | 0 |
| [`ch16.1`](ch16.1/) | Choosing, Integers and Floats | How Python's number types represent values and combine in arithmetic; Why Python integers have no… | 1 | 13 | 0 |
| [`ch16.2`](ch16.2/) | Rounding Floats and Exact Decimals | The difference between truncating, flooring, ceiling and rounding, and why `round(0.5)` is `0`; `Decimal`… | 0 | 11 | 0 |
| [`ch16.3`](ch16.3/) | Fractions and Complex Numbers | How `Fraction` keeps exact ratios, and what a Fraction built from a float holds; How to convert a ratio… | 0 | 7 | 0 |
| [`ch16.4`](ch16.4/) | bool, Truthiness and Short-Circuiting | Why `True + True` is `2`, and how `sum()` counts `True` values; Which common built-in values are falsy;… | 0 | 6 | 0 |
| [`ch17.1`](ch17.1/) | Scopes, LEGB and Local Names | What a scope is, and why a name made inside a function cannot be used outside it; How LEGB orders local,… | 0 | 8 | 0 |
| [`ch17.2`](ch17.2/) | Nested Functions, nonlocal and Closures | How a nested function reads and changes the bindings of its enclosing function with `nonlocal`; What a… | 0 | 14 | 0 |
| [`ch17.3`](ch17.3/) | Higher-Order Functions, Inspection and reduce | What a higher-order function is, and how to inspect a function like any other object; How… | 0 | 11 | 0 |
| [`ch17.4`](ch17.4/) | partial, operator, Combining and Lambdas | How `functools.partial` pre-fills arguments, how to inspect it, and how `Placeholder` reserves a position;… | 0 | 12 | 0 |
| [`ch18.1`](ch18.1/) | Writing a Decorator, @ and wraps | The problem decorators solve, and why they save you from editing every function by hand; How to build a… | 0 | 8 | 0 |
| [`ch18.2`](ch18.2/) | Timer, Logger, Stacking and Memoization | How to write a timer and a logger, and how to stack several decorators together; Why decorator order changes… | 0 | 11 | 0 |
| [`ch18.3`](ch18.3/) | Decorator Factories and Validation | How to write a decorator that takes its own arguments (a decorator factory); How a registration decorator… | 1 | 8 | 0 |
| [`ch18.4`](ch18.4/) | Dispatching and Common Uses | How to make one function behave differently depending on the *type* of its argument (dispatching); How an… | 0 | 6 | 0 |
| [`ch19.1`](ch19.1/) | Tuples as Records, Unpacking and Immutability | How to use a tuple as a **record**, where each position has a meaning; How to read a tuple with unpacking,… | 1 | 10 | 0 |
| [`ch19.2`](ch19.2/) | Creating and Using namedtuple | `namedtuple`: giving each position in a tuple a real name; How to read a field by name or by position, and… | 0 | 11 | 0 |
| [`ch19.3`](ch19.3/) | Defaults, Extending and Real Uses | How `defaults` fill the rightmost fields, and why a mutable default is shared; How to give a record type… | 0 | 7 | 0 |
| [`ch20.1`](ch20.1/) | Import Steps, Module Objects and sys.modules | What Python does when it runs `import something`; Why a module is an object and how to inspect it; Why a… | 16 | 6 | 0 |
| [`ch20.2`](ch20.2/) | sys.path, Finders and Import Forms | Where Python looks for modules with `sys.path`, and how a local file can hide a standard module; What… | 16 | 4 | 0 |
| [`ch20.3`](ch20.3/) | Reloading Modules and the Main Guard | How to reload a module, and why you rarely should; How `if __name__ == "__main__":` and the direct-run name… | 8 | 3 | 0 |
| [`ch20.4`](ch20.4/) | Packages and Project Structure | What a package is, what `__init__.py` is for, and how `__all__` selects star-import names; How to structure… | 36 | 2 | 0 |
| [`ch20.5`](ch20.5/) | Namespace Packages, ZIP Imports and Installation | What namespace packages are and how they combine directory portions; How Python imports code from a ZIP… | 16 | 1 | 0 |
| [`ch20.6`](ch20.6/) | Depth Sessions and Composed Practice | How to prepare, register, run and clean up a module namespace by hand; How to follow module references and… | 27 | 1 | 0 |
| [`ch20a`](ch20a/) | Project - Command-line labels library | Prerequisite: Start this required inline visit after the import, package and namespace foundations in lesson… | 6 | 0 | 0 |
| [`ch20b`](ch20b/) | Project - Shop-report package build and installation | Prerequisite: Start this required inline visit after lesson 20's import, package-context and cache sections,… | 3 | 0 | 3 |
| [`ch20c`](ch20c/) | Checkpoint - Imports and packages | This part explains why Python behaves in these ways. Use the checkpoint to test both your memory and your… | 2 | 3 | 0 |

## 03 - Objects, protocols and testing

| Folder | Chapter | What it teaches | Saved files | Examples | Commands |
|---|---|---|---|---|---|
| [`ch21.1`](ch21.1/) | Classes, Objects and Instance Attributes | Why classes exist: keeping data and the functions that work on it together; How to define a class and create… | 0 | 8 | 0 |
| [`ch21.2`](ch21.2/) | Class Attributes and Methods | How a class attribute is shared, and how an instance can shadow it; Why a mutable class attribute can cause… | 1 | 9 | 0 |
| [`ch21.3`](ch21.3/) | Callable Classes and Runtime Attributes | Why a class is callable, and why `int` is a class too; How `type` and `isinstance` ask different questions;… | 0 | 12 | 0 |
| [`ch21.4`](ch21.4/) | Properties, Validation and Caching | Why a bare attribute gives no control over a new value; How `@property` and `@x.setter` run a method on read… | 1 | 17 | 0 |
| [`ch21.5`](ch21.5/) | Class Methods, Static Methods and the Class Body | How `@classmethod` and `cls` build an alternative constructor; How `@staticmethod` groups a helper with the… | 0 | 14 | 0 |
| [`ch22.1`](ch22.1/) | What Dunder Methods Are, Text, Bytes and Operators | What dunder methods are and which Python operations call them; How `__str__` and `__repr__` give text for… | 0 | 10 | 0 |
| [`ch22.2`](ch22.2/) | Hashing, Truth, Calls and Formats | Why `__eq__` and `__hash__` must agree, and what breaks in dicts and sets if they do not; How `__bool__` and… | 0 | 12 | 0 |
| [`ch22.3`](ch22.3/) | Cleanup, Indexing and the Overview Table | Why `__del__` should not be trusted for cleanup; What `__getitem__` adds: indexing and slicing; How… | 0 | 3 | 0 |
| [`ch22.4`](ch22.4/) | Operator Overloading with Mixed Types | How Python picks the method that runs for `a + b`; How `NotImplemented` differs from `NotImplementedError`;… | 0 | 21 | 0 |
| [`ch23.1`](ch23.1/) | Inheritance, Overriding and super() | How a child class can reuse methods and class attributes from a parent class; How overriding replaces a… | 1 | 10 | 0 |
| [`ch23.2`](ch23.2/) | Composition and the Four Pillars of OOP | When inheritance is the right tool, and when composition is better; The four pillars of OOP in plain words:… | 0 | 13 | 0 |
| [`ch23.3`](ch23.3/) | Method Resolution Order, Mixins and Slots | The Method Resolution Order (MRO): the order Python searches for a method; How multiple inheritance, C3 and… | 6 | 6 | 0 |
| [`ch23.4`](ch23.4/) | The Diamond and Cooperative super() | Why naming the parent class in each method runs a shared grandparent twice; How `super()` selects the next… | 3 | 6 | 0 |
| [`ch23a`](ch23a/) | Project - Records with Behavior - Person, Manager and Department | Before the second session, revisit Favour composition over inheritance. Read the neutral problem, fix, and… | 5 | 2 | 0 |
| [`ch24.1`](ch24.1/) | Exception Families and Why Make Your Own | The main branches of Python's built-in exception tree, and why normal handlers catch `Exception` instead of… | 0 | 5 | 0 |
| [`ch24.2`](ch24.2/) | Exception Data, Behavior and Hierarchies | What an exception class, an instance, its message and its `args` are; How to add extra data to an exception,… | 1 | 18 | 0 |
| [`ch24.3`](ch24.3/) | Nested Handlers, Causes and Recovery | Following nested handlers and distinguishing stored diagnostic information from traceback display; `raise… | 0 | 15 | 0 |
| [`ch24.4`](ch24.4/) | Diagnosing and Repairing an Inventory | How a small module defines an exception family and handles it; How a missing check lets invalid quantities… | 0 | 5 | 0 |
| [`ch24.5`](ch24.5/) | Account Identity and Overdraft Decisions | How to build an `Account` with read-only properties, an identifier and an opening ledger entry; How equality… | 0 | 7 | 0 |
| [`ch25.1`](ch25.1/) | Why Tests Exist, What a Test Is and Running pytest | Why tests are useful and which problems they help you find; What a test is, in plain words, and how `assert`… | 3 | 2 | 0 |
| [`ch25.2`](ch25.2/) | What to Test, Parametrize, State Checks and Fixtures | The three kinds of case a function needs: normal, edge and error; How `pytest.raises` checks an error and… | 12 | 10 | 2 |
| [`ch25.3`](ch25.3/) | unittest, doctest and Mocks | How `unittest` organises tests as `TestCase` methods, and how it compares with pytest; How `setUp`,… | 12 | 5 | 0 |
| [`ch25.4`](ch25.4/) | Coverage, TDD and a Callable Boundary | What line coverage measures, and why 100% coverage does not prove correctness; How red, green, refactor… | 9 | 3 | 0 |
| [`ch25a`](ch25a/) | Project - Parsing Records Before Publishing Data | How to parse a small CSV policy into date/`Decimal` observation records; Why a complete candidate tuple must… | 4 | 0 | 0 |
| [`ch25b`](ch25b/) | Project - Testing a Timer with Two Clocks | How a `Timer` has idle, running, and stopped states; Why duration needs a monotonic counter while timestamps… | 5 | 0 | 0 |
| [`ch25c`](ch25c/) | Project - Modular Values and Operator Contracts | How to do arithmetic while keeping old aliases and dictionary keys unchanged; Why mathematical congruence,… | 7 | 0 | 0 |
| [`ch25d`](ch25d/) | Project - Inventory Inheritance and Regression Tests | How one stock invariant can govern five related concrete classes; How `super()` lets several initializers… | 13 | 0 | 0 |
| [`ch26`](ch26/) | Interfaces - Duck Typing, ABCs and Protocols | What an interface means in Python, which has no `interface` keyword; How **duck typing** works and why… | 0 | 33 | 4 |
| [`ch26a`](ch26a/) | Project - Composing Readers, Converters and Writers | Compose three small roles around one unchanged processing function.; Separate a valid record from an… | 7 | 0 | 0 |
| [`ch27`](ch27/) | Callable Objects and Class Decorators | Distinguish callable objects from calls with valid arguments.; Build attribute and method tools, and reason… | 2 | 27 | 0 |
| [`ch28`](ch28/) | Record Classes, Dataclasses and Identity | Add methods to records made with `namedtuple`.; Compare records made with `collections.namedtuple`,… | 7 | 16 | 0 |
| [`ch29`](ch29/) | Descriptors | How one mechanism supports `@property`, methods, and `__slots__`; What a **descriptor** is and which three… | 1 | 27 | 0 |
| [`ch29a`](ch29a/) | Project - Counting Calls Without Losing the Receiver | A call counter needs to know both which operation ran and which inventory received it. Start with a… | 6 | 0 | 0 |
| [`ch30`](ch30/) | Enums | Why repeated unexplained numbers and strings can cause bugs; How to define an **enumeration**, or enum, with… | 3 | 43 | 0 |
| [`ch31`](ch31/) | Metaclasses and Metaprogramming | What a metaclass is and how it relates to a class object; How `type` acts as the default metaclass, and how… | 26 | 27 | 0 |
| [`ch31a`](ch31a/) | Project - Validated Fields - Preserve Behavior While Refactoring | A reusable field needs more than a valid-value example. Its callers also rely on omitted arguments, error… | 7 | 0 | 0 |
| [`ch31b`](ch31b/) | Project - Display and Delegate Records | The first record application prints a manager with the hardcoded label `Person`. Continue that same… | 9 | 0 | 0 |
| [`ch31c`](ch31c/) | Project - Attribute Policies Through a Wrapper | Build a wrapper that checks selected attribute reads and writes before they reach another object.… | 9 | 0 | 0 |

## 04 - Iteration and resource management

| Folder | Chapter | What it teaches | Saved files | Examples | Commands |
|---|---|---|---|---|---|
| [`ch32`](ch32/) | The Sequence Protocol and Custom Sequences | What a **protocol** is and how Python uses supported operations; How `__len__` and `__getitem__` provide the… | 5 | 30 | 0 |
| [`ch32a`](ch32a/) | Project - From a Read-Only Deck to a Mutable Sequence | How a small `__len__`/`__getitem__` interface already enables several sequence fallbacks; Why shuffle needs… | 7 | 0 | 0 |
| [`ch33`](ch33/) | Iterables and Iterators | How one protocol lets `for` work with lists, strings, files, dictionaries, and your own classes; The… | 3 | 18 | 0 |
| [`ch33a`](ch33a/) | Project - Forwarding Selected Python Operations | Why direct special-method lookup can succeed while an operator still fails; How to forward five selected… | 6 | 0 | 0 |
| [`ch33b`](ch33b/) | Project - Reuse a Finite Forwarding Interface | How explicit mixins, a small router, and descriptors reuse the same five forwarding operations; When an… | 7 | 0 | 0 |
| [`ch33c`](ch33c/) | Project - When Inserting Hooks Changes the Contract | How replacing hooks on an existing class retains class identity while changing behavior; Why object-level… | 5 | 0 | 0 |
| [`ch34`](ch34/) | Generators | How generators replace a manual iterator class; How `yield` changes a function call and pauses execution;… | 0 | 22 | 0 |
| [`ch34a`](ch34a/) | Project - A Shared Contract for Random Draws | How an abstract base class defines a small random-draw contract; How three classes can meet one contract… | 7 | 0 | 0 |
| [`ch34b`](ch34b/) | Project - Calling and Combining Random Containers | Why removing a value is different from returning it from a callable; How `+` and `+=` have different… | 5 | 0 | 0 |
| [`ch35`](ch35/) | The itertools Toolbox | What `itertools` provides, which tools read input immediately, and which tools produce output lazily; How to… | 0 | 44 | 0 |
| [`ch35a`](ch35a/) | Project - Accounts and Transaction Confirmations | How account-specific state composes with a fixed display offset and shared class settings; How to compare… | 8 | 0 | 0 |
| [`ch36`](ch36/) | Context Managers | Why a program must release resources after success or failure; How `try`/`finally` guarantees cleanup; How… | 4 | 30 | 0 |

## 05 - Runtime

| Folder | Chapter | What it teaches | Saved files | Examples | Commands |
|---|---|---|---|---|---|
| [`ch37`](ch37/) | Object Lifetime and Memory Management | Explain CPython reference counts and unreachable reference cycles.; Find caches and callbacks that keep… | 3 | 16 | 0 |
| [`ch38`](ch38/) | How Python Runs Your Code | How Python turns source text into instructions and runs them; How to inspect each stage with the `tokenize`,… | 5 | 34 | 0 |
| [`ch38a`](ch38a/) | Checkpoint - Python runtime | 1. Which identity rules does Python promise? Which memory details belong only to CPython? | 0 | 1 | 0 |

## 06 - Containers and data boundaries

| Folder | Chapter | What it teaches | Saved files | Examples | Commands |
|---|---|---|---|---|---|
| [`ch39`](ch39/) | Hash Tables and Dictionaries in Depth | What an "associative array" is, and why `dict` is Python's version of it; How Python uses a hash table to… | 2 | 30 | 0 |
| [`ch40`](ch40/) | Sets in Depth | Basic set operations: membership, subset, union, intersection, and difference; Why set membership is usually… | 1 | 22 | 0 |
| [`ch41`](ch41/) | Specialized Dictionaries | Why the `collections` module exists and when to use it instead of `dict`; How `defaultdict` creates values… | 2 | 32 | 0 |
| [`ch42`](ch42/) | Serialization | What serialization is and why programs use it; `pickle` — Python's own format, what it can do, and its… | 11 | 25 | 0 |
| [`ch42a`](ch42a/) | Project - Store and Reopen Records | Continue the `Person`/`Manager` application across program runs. Save records under stable string IDs,… | 16 | 0 | 0 |
| [`ch42b`](ch42b/) | Checkpoint - Containers and serialization | 1. What does "hashable" actually require? Is it the same as "immutable"? | 1 | 2 | 0 |

## 07 - Concurrency

| Folder | Chapter | What it teaches | Saved files | Examples | Commands |
|---|---|---|---|---|---|
| [`ch43`](ch43/) | From Coroutines to async-await | What a **coroutine** is, and how it compares with threads and processes; How to write modern async code with… | 15 | 36 | 0 |
| [`ch43a`](ch43a/) | Checkpoint - Iteration and async | 1. What is the difference between an iterable and an iterator — and is an iterator an iterable? | 0 | 4 | 0 |
| [`ch44`](ch44/) | Threads, Locks and Race Conditions | What processes and threads are, and how they differ; Concurrency vs parallelism, and why threads on the… | 9 | 13 | 0 |
| [`ch45`](ch45/) | Multiprocessing and Pools | Why GIL-enabled CPython threads do not execute pure-Python bytecode on several cores simultaneously, and how… | 8 | 14 | 0 |

## 08 - Professional diagnostics

| Folder | Chapter | What it teaches | Saved files | Examples | Commands |
|---|---|---|---|---|---|
| [`ch46`](ch46/) | Logging | Why logs are more useful than many temporary `print()` statements; The five severity levels, and why a… | 0 | 13 | 0 |
| [`ch47`](ch47/) | Debugging and Profiling | How to reproduce a wrong result, pause a program with `pdb`, and inspect the control flow that produced it;… | 4 | 1 | 0 |
| [`ch48`](ch48/) | Checking and Building a Python Package | What formatting, linting, static types, tests and builds each check; How to observe an actual failure and… | 6 | 0 | 9 |

## 09 - Data and database applications

| Folder | Chapter | What it teaches | Saved files | Examples | Commands |
|---|---|---|---|---|---|
| [`ch49`](ch49/) | NumPy | Why plain Python lists are slow for number-crunching, and what NumPy does differently; What an array, a… | 4 | 37 | 0 |
| [`ch50`](ch50/) | Pandas | What pandas is for, and when to reach for it instead of NumPy; The two core objects: `Series` and… | 4 | 37 | 0 |
| [`ch51`](ch51/) | Visualization - Matplotlib and Seaborn | Why a picture can show you things a table of numbers hides; The two ways to use matplotlib, and why the… | 0 | 24 | 0 |
| [`ch52`](ch52/) | SQLite from Python | Why plain files and CSV stop being enough once a program grows; What SQLite is, and how Python exposes it… | 0 | 17 | 0 |
| [`ch52a`](ch52a/) | Boundary visit - SQL values and commands | First finish lesson 52 through the basic SQL examples. You should be able to create a table, insert rows and… | 0 | 5 | 0 |
| [`ch52b`](ch52b/) | Project - SQLite expense tracker | Prerequisite: Finish lesson 52's connection, transaction and basic SQL teaching, then the SQL values visit's… | 0 | 1 | 0 |

## 10 - Web applications and production boundaries

| Folder | Chapter | What it teaches | Saved files | Examples | Commands |
|---|---|---|---|---|---|
| [`ch53`](ch53/) | Flask - Your First Web App | How a browser and a web server exchange requests and responses; What `Flask` is, and how to write the… | 15 | 6 | 0 |
| [`ch53a`](ch53a/) | Project - Internal Diagnostics and Public Responses | Give related failures a useful exception hierarchy and a consistent message contract.; Capture one event… | 7 | 0 | 0 |
| [`ch53b`](ch53b/) | Project - Two-page Flask notes app | Prerequisite: Start this required inline visit after lesson 53 has installed `Flask` and introduced the… | 2 | 0 | 0 |
| [`ch54`](ch54/) | REST APIs, requests and Web Scraping | What an API is and how REST APIs use URLs and HTTP methods; How to call an API with the `requests` library,… | 16 | 12 | 0 |
| [`ch54a`](ch54a/) | Boundary visit - HTTP status and error handling | Prerequisite: Start this required inline visit after lesson 54 has introduced the `requests` library and a… | 0 | 1 | 0 |
| [`ch54b`](ch54b/) | Project - Loading a Consistent Resource Snapshot | Load a response only when its body, size or duration is first needed.; Keep those values together so that… | 5 | 0 | 0 |
| [`ch54c`](ch54c/) | Boundary visit - HTTP Resources and Retry Policy | Finish weather and the response-cache visit first. Refresh context entry, cleanup and exception propagation,… | 4 | 0 | 0 |
| [`ch54d`](ch54d/) | Checkpoint - Applied Python | This part includes mistakes that can lose money or expose private data. Review it carefully. | 0 | 3 | 0 |
| [`ch54e`](ch54e/) | Capstone - Configuring and Operating an Expense Ledger | This capstone joins settings, a command line, validation, transactions, logs, tests, packaging and an… | 17 | 2 | 6 |

## 11 - Design, craft and next steps

| Folder | Chapter | What it teaches | Saved files | Examples | Commands |
|---|---|---|---|---|---|
| [`ch55`](ch55/) | Writing Effective Python | 39 ways to review and improve Python code; When each habit helps, what it costs, and when another choice may… | 5 | 55 | 0 |
| [`ch55a`](ch55a/) | Checkpoint - Effective Python | 1. What does `@dataclass(frozen=True)` actually stop you doing — and what does it not? | 0 | 2 | 0 |

## How the folders are made

A tool reads each certified chapter and copies its code: Python files whose first line names them (`# report.py`), project files marked for the package and capstone chapters (`pyproject.toml`, `requirements-dev.txt`, `RUNBOOK.md`), HTML templates, every other Python block as a numbered example, and every bash or PowerShell block. Nothing is hand-edited here; when a chapter changes, the folders are regenerated. No file holds a key, a token or a password.
