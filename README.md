# pythonbook

The files the chapters of the **Python tutorial** (the LearnAIConcepts programme) ask the reader to save, one folder per chapter, extracted byte for byte from each certified chapter. Nothing here is meant to be read on its own: read the chapter, which explains every line. Every example was run on **Python 3.15.0** by the tutorial's code gate.

Chapters whose examples are all short snippets typed at the prompt have no folder. A folder's own `README.md` lists its files (`ABOUT.md` where the chapter's project has a README of its own); where a chapter saves a file twice, the folder keeps the version the chapter ends with.

## 01 - Orientation

| Folder | Chapter | Files |
|---|---|---|
| `ch02` | Setting Up Your Python Workshop | 5 |

## 02 - Language and first tools

| Folder | Chapter | Files |
|---|---|---|
| `ch10` | Errors and Exceptions | 5 |
| `ch11` | Modules, Packages and Files | 8 |
| `ch12` | The Standard Library Tour | 4 |
| `ch14` | Text, Bytes and Encodings | 6 |
| `ch16` | Numbers in Depth | 1 |
| `ch18` | Function Decorators | 1 |
| `ch19` | Tuples and Named Tuples | 1 |
| `ch20` | The Import System in Depth | 119 |
| `ch20a` | Project - Command-line labels library | 6 |
| `ch20b` | Project - Shop-report package build and installation | 3 |
| `ch20c` | Checkpoint - Imports and packages | 2 |

## 03 - Objects, protocols and testing

| Folder | Chapter | Files |
|---|---|---|
| `ch21` | Classes and Objects | 2 |
| `ch23` | Inheritance and Polymorphism | 10 |
| `ch23a` | Project - Records with Behavior - Person, Manager and Department | 5 |
| `ch24` | Custom Exceptions | 1 |
| `ch25` | Testing Your Code | 30 |
| `ch25a` | Project - Parsing Records Before Publishing Data | 4 |
| `ch25b` | Project - Testing a Timer with Two Clocks | 5 |
| `ch25c` | Project - Modular Values and Operator Contracts | 7 |
| `ch25d` | Project - Inventory Inheritance and Regression Tests | 13 |
| `ch26a` | Project - Composing Readers, Converters and Writers | 7 |
| `ch27` | Callable Objects and Class Decorators | 2 |
| `ch28` | Record Classes, Dataclasses and Identity | 7 |
| `ch29` | Descriptors | 1 |
| `ch29a` | Project - Counting Calls Without Losing the Receiver | 6 |
| `ch30` | Enums | 3 |
| `ch31` | Metaclasses and Metaprogramming | 26 |
| `ch31a` | Project - Validated Fields - Preserve Behavior While Refactoring | 7 |
| `ch31b` | Project - Display and Delegate Records | 9 |
| `ch31c` | Project - Attribute Policies Through a Wrapper | 9 |

## 04 - Iteration and resource management

| Folder | Chapter | Files |
|---|---|---|
| `ch32` | The Sequence Protocol and Custom Sequences | 5 |
| `ch32a` | Project - From a Read-Only Deck to a Mutable Sequence | 7 |
| `ch33` | Iterables and Iterators | 3 |
| `ch33a` | Project - Forwarding Selected Python Operations | 6 |
| `ch33b` | Project - Reuse a Finite Forwarding Interface | 7 |
| `ch33c` | Project - When Inserting Hooks Changes the Contract | 5 |
| `ch34a` | Project - A Shared Contract for Random Draws | 7 |
| `ch34b` | Project - Calling and Combining Random Containers | 5 |
| `ch35a` | Project - Accounts and Transaction Confirmations | 8 |
| `ch36` | Context Managers | 4 |

## 05 - Runtime

| Folder | Chapter | Files |
|---|---|---|
| `ch37` | Object Lifetime and Memory Management | 3 |
| `ch38` | How Python Runs Your Code | 5 |

## 06 - Containers and data boundaries

| Folder | Chapter | Files |
|---|---|---|
| `ch39` | Hash Tables and Dictionaries in Depth | 2 |
| `ch40` | Sets in Depth | 1 |
| `ch41` | Specialized Dictionaries | 2 |
| `ch42` | Serialization | 11 |
| `ch42a` | Project - Store and Reopen Records | 16 |
| `ch42b` | Checkpoint - Containers and serialization | 1 |

## 07 - Concurrency

| Folder | Chapter | Files |
|---|---|---|
| `ch43` | From Coroutines to async-await | 15 |
| `ch44` | Threads, Locks and Race Conditions | 9 |
| `ch45` | Multiprocessing and Pools | 8 |

## 08 - Professional diagnostics

| Folder | Chapter | Files |
|---|---|---|
| `ch47` | Debugging and Profiling | 4 |
| `ch48` | Checking and Building a Python Package | 6 |

## 09 - Data and database applications

| Folder | Chapter | Files |
|---|---|---|
| `ch49` | NumPy | 4 |
| `ch50` | Pandas | 4 |

## 10 - Web applications and production boundaries

| Folder | Chapter | Files |
|---|---|---|
| `ch53` | Flask - Your First Web App | 15 |
| `ch53a` | Project - Internal Diagnostics and Public Responses | 7 |
| `ch53b` | Project - Two-page Flask notes app | 2 |
| `ch54` | REST APIs, requests and Web Scraping | 16 |
| `ch54b` | Project - Loading a Consistent Resource Snapshot | 5 |
| `ch54c` | Boundary visit - HTTP Resources and Retry Policy | 4 |
| `ch54e` | Capstone - Configuring and Operating an Expense Ledger | 17 |

## 11 - Design, craft and next steps

| Folder | Chapter | Files |
|---|---|---|
| `ch55` | Writing Effective Python | 5 |

## How the folders are made

A tool reads each certified chapter and copies every block the chapter tells you to save: Python files whose first line names them (`# report.py`), project files marked for the package and capstone chapters (`pyproject.toml`, `requirements-dev.txt`, `RUNBOOK.md`), and HTML templates. Nothing is hand-edited here; when a chapter changes, the folders are regenerated. No file holds a key, a token or a password.
