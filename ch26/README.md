# 26 - Interfaces - Duck Typing, ABCs and Protocols

The code of the chapter **26 - Interfaces - Duck Typing, ABCs and Protocols** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What an interface means in Python, which has no `interface` keyword
- How **duck typing** works and why missing-method errors can appear late
- **Goose typing**: using `isinstance` against an abstraction instead of a concrete class
- The main `collections.abc` classes and the dunder methods each one requires
- Writing your own **abstract base class (ABC)** with `abc.ABC` and `@abstractmethod`
- How `.register()` makes a **virtual subclass** without adding inheritance
- `__subclasshook__` — how some ABCs recognize a matching class with no registration either
- `typing.Protocol` — Python's modern, structural answer to the same problem
- How to pick between duck typing, an ABC, a `Protocol`, and `.register()`

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_duck-typing-use-operations-without-checking-a-cl.py` | Duck typing: use operations without checking a class (line 78) | runs on its own |
| `examples/02_method-names-are-not-the-whole-cache-contract.py` | Duck typing: use operations without checking a class › Method names are not the whole cache contract (line 127) | runs on its own |
| `examples/03_method-names-are-not-the-whole-cache-contract.py` | Duck typing: use operations without checking a class › Method names are not the whole cache contract (line 176) | runs on its own |
| `examples/04_the-exact-weakness-errors-arrive-late.py` | Duck typing: use operations without checking a class › The exact weakness: errors arrive late (line 214) | runs on its own |
| `examples/05_python-s-own-duck-typing-trick-the-sequence-prot.py` | Duck typing: use operations without checking a class › Python's own duck typing trick: the sequence protocol (line 252) | runs on its own |
| `examples/06_iteration-can-succeed-without-iterable-recogniti.py` | Duck typing: use operations without checking a class › Iteration can succeed without `Iterable` recognition (line 294) | may use names from earlier examples |
| `examples/07_iteration-can-succeed-without-iterable-recogniti.py` | Duck typing: use operations without checking a class › Iteration can succeed without `Iterable` recognition (line 327) | may use names from earlier examples |
| `examples/08_goose-typing-isinstance-against-an-abstraction.py` | Goose typing: `isinstance` against an abstraction (line 352) | runs on its own |
| `examples/09_standard-interfaces-in-collections-abc.py` | Standard interfaces in `collections.abc` (line 391) | runs on its own |
| `examples/10_standard-interfaces-in-collections-abc.py` | Standard interfaces in `collections.abc` (line 440) | runs on its own |
| `examples/11_standard-interfaces-in-collections-abc.py` | Standard interfaces in `collections.abc` (line 475) | runs on its own |
| `examples/12_numeric-contracts-the-numbers-abc-tower.py` | Standard interfaces in `collections.abc` › Numeric contracts: the `numbers` ABC tower (line 521) | runs on its own |
| `examples/13_writing-your-own-abc.py` | Writing your own ABC (line 559) | runs on its own |
| `examples/14_an-abstract-method-can-sit-beside-a-working-one.py` | Writing your own ABC › An abstract method can sit beside a working one (line 596) | runs on its own |
| `examples/15_an-abstract-method-can-sit-beside-a-working-one.py` | Writing your own ABC › An abstract method can sit beside a working one (line 654) | runs on its own |
| `examples/16_an-abstract-method-can-sit-beside-a-working-one.py` | Writing your own ABC › An abstract method can sit beside a working one (line 689) | runs on its own |
| `examples/17_an-abstract-method-can-sit-beside-a-working-one.py` | Writing your own ABC › An abstract method can sit beside a working one (line 734) | runs on its own |
| `examples/18_virtual-subclasses-register.py` | Virtual subclasses: `.register()` (line 816) | runs on its own |
| `examples/19_virtual-subclasses-register.py` | Virtual subclasses: `.register()` (line 866) | runs on its own |
| `examples/20_virtual-subclasses-register.py` | Virtual subclasses: `.register()` (line 917) | runs on its own |
| `examples/21_virtual-subclasses-register.py` | Virtual subclasses: `.register()` (line 951) | runs on its own |
| `examples/22_virtual-subclasses-register.py` | Virtual subclasses: `.register()` (line 995) | runs on its own |
| `examples/23_subclasshook-isinstance-with-no-registration-eit.py` | `__subclasshook__`: `isinstance` with no registration either (line 1031) | runs on its own |
| `examples/24_subclasshook-isinstance-with-no-registration-eit.py` | `__subclasshook__`: `isinstance` with no registration either (line 1056) | runs on its own |
| `examples/25_typing-protocol-structural-typing-pep-544.py` | `typing.Protocol`: structural typing (PEP 544) (line 1134) | runs on its own |
| `examples/26_runtime-checkable-and-its-real-limit.py` | `typing.Protocol`: structural typing (PEP 544) › `@runtime_checkable` and its real limit (line 1182) | runs on its own |
| `examples/27_use-a-saved-file-to-check-a-signature-before-run.py` | `typing.Protocol`: structural typing (PEP 544) › Use a saved file to check a signature before running it (line 1245) | runs on its own |
| `examples/28_use-a-saved-file-to-check-a-signature-before-run.py` | `typing.Protocol`: structural typing (PEP 544) › Use a saved file to check a signature before running it (line 1318) | a fragment, not a complete program |
| `examples/29_a-member-can-exist-without-being-callable.py` | `typing.Protocol`: structural typing (PEP 544) › A member can exist without being callable (line 1340) | runs on its own |
| `examples/30_method-bodies-in-a-protocol.py` | `typing.Protocol`: structural typing (PEP 544) › Method bodies in a Protocol (line 1388) | runs on its own |
| `examples/31_method-bodies-in-a-protocol.py` | `typing.Protocol`: structural typing (PEP 544) › Method bodies in a Protocol (line 1420) | runs on its own |
| `examples/32_check-the-same-behavior-across-implementations.py` | Choosing an approach › Check the same behavior across implementations (line 1536) | runs on its own |
| `examples/33_try-it-yourself.py` | Try it yourself (line 1652) | runs on its own |

## Terminal commands

| File | Where it is in the chapter | Note |
|---|---|---|
| `commands/01_use-a-saved-file-to-check-a-signature-before-run.ps1` | `typing.Protocol`: structural typing (PEP 544) › Use a saved file to check a signature before running it (line 1230) | powershell commands to type in a terminal |
| `commands/02_use-a-saved-file-to-check-a-signature-before-run.ps1` | `typing.Protocol`: structural typing (PEP 544) › Use a saved file to check a signature before running it (line 1282) | powershell commands to type in a terminal |
| `commands/03_use-a-saved-file-to-check-a-signature-before-run.ps1` | `typing.Protocol`: structural typing (PEP 544) › Use a saved file to check a signature before running it (line 1301) | powershell commands to type in a terminal |
| `commands/04_method-bodies-in-a-protocol.ps1` | `typing.Protocol`: structural typing (PEP 544) › Method bodies in a Protocol (line 1459) | powershell commands to type in a terminal |
