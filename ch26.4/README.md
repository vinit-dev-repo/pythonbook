# 26.4 - Protocols and Choosing an Approach

The code of the chapter **26.4 - Protocols and Choosing an Approach** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How `typing.Protocol` describes a shape without changing the matching class
- What `@runtime_checkable` checks, and why it does not check signatures
- How to run mypy on a saved file to catch a wrong signature before the program runs
- Why a `Protocol` body is not inherited by a class that only matches the structure
- How to choose between duck typing, a base class, an ABC, `.register()`, a `Protocol` and an adapter, and how one behavior check tests several implementations

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_typing-protocol-structural-typing-pep-544.py` | `typing.Protocol`: structural typing (PEP 544) (line 49) | runs on its own |
| `examples/02_runtime-checkable-and-its-real-limit.py` | `typing.Protocol`: structural typing (PEP 544) › `@runtime_checkable` and its real limit (line 92) | runs on its own |
| `examples/03_use-a-saved-file-to-check-a-signature-before-run.py` | `typing.Protocol`: structural typing (PEP 544) › Use a saved file to check a signature before running it (line 151) | runs on its own |
| `examples/04_use-a-saved-file-to-check-a-signature-before-run.py` | `typing.Protocol`: structural typing (PEP 544) › Use a saved file to check a signature before running it (line 218) | a fragment, not a complete program |
| `examples/05_a-member-can-exist-without-being-callable.py` | `typing.Protocol`: structural typing (PEP 544) › A member can exist without being callable (line 240) | runs on its own |
| `examples/06_method-bodies-in-a-protocol.py` | `typing.Protocol`: structural typing (PEP 544) › Method bodies in a Protocol (line 281) | runs on its own |
| `examples/07_method-bodies-in-a-protocol.py` | `typing.Protocol`: structural typing (PEP 544) › Method bodies in a Protocol (line 313) | runs on its own |
| `examples/08_check-the-same-behavior-across-implementations.py` | Choosing an approach › Check the same behavior across implementations (line 428) | runs on its own |
| `examples/09_try-it-yourself.py` | Try it yourself (line 534) | runs on its own |

## Terminal commands

| File | Where it is in the chapter | Note |
|---|---|---|
| `commands/01_use-a-saved-file-to-check-a-signature-before-run.ps1` | `typing.Protocol`: structural typing (PEP 544) › Use a saved file to check a signature before running it (line 134) | powershell commands to type in a terminal |
| `commands/02_use-a-saved-file-to-check-a-signature-before-run.ps1` | `typing.Protocol`: structural typing (PEP 544) › Use a saved file to check a signature before running it (line 183) | powershell commands to type in a terminal |
| `commands/03_use-a-saved-file-to-check-a-signature-before-run.ps1` | `typing.Protocol`: structural typing (PEP 544) › Use a saved file to check a signature before running it (line 201) | powershell commands to type in a terminal |
| `commands/04_method-bodies-in-a-protocol.ps1` | `typing.Protocol`: structural typing (PEP 544) › Method bodies in a Protocol (line 346) | powershell commands to type in a terminal |
