# 20.5 - Namespace Packages, ZIP Imports and Installation

The code of the chapter **20.5 - Namespace Packages, ZIP Imports and Installation** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What namespace packages are and how they combine directory portions
- How Python imports code from a ZIP file, and why that is not installation
- Where the command-line library and the build-and-install workflow continue
- How to install a src-layout project, build a wheel, and test it in a fresh consumer environment

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `namespace_demo/dir1/tools/alpha.py` | Namespace packages: packages without `__init__.py` (line 45) |  |
| `namespace_demo/dir2/tools/beta.py` | Namespace packages: packages without `__init__.py` (line 50) |  |
| `namespace_demo/check.py` | Namespace packages: packages without `__init__.py` (line 56) |  |
| `namespace_demo/regular/tools/__init__.py` | Namespace packages: packages without `__init__.py` (line 86) |  |
| `namespace_demo/check_regular.py` | Namespace packages: packages without `__init__.py` (line 91) |  |
| `namespace_growth/dir1/tools/alpha.py` | Namespace packages: packages without `__init__.py` › A namespace search path can grow (line 116) |  |
| `namespace_growth/dir2/tools/beta.py` | Namespace packages: packages without `__init__.py` › A namespace search path can grow (line 122) |  |
| `namespace_growth/dir1/tools/shared/first.py` | Namespace packages: packages without `__init__.py` › A namespace search path can grow (line 127) |  |
| `namespace_growth/dir2/tools/shared/second.py` | Namespace packages: packages without `__init__.py` › A namespace search path can grow (line 132) |  |
| `namespace_growth/dir2/tools/regular/__init__.py` | Namespace packages: packages without `__init__.py` › A namespace search path can grow (line 137) |  |
| `namespace_growth/concrete/tools.py` | Namespace packages: packages without `__init__.py` › A namespace search path can grow (line 142) |  |
| `namespace_growth/check.py` | Namespace packages: packages without `__init__.py` › A namespace search path can grow (line 147) |  |
| `namespace_growth/check_concrete.py` | Namespace packages: packages without `__init__.py` › A namespace search path can grow (line 193) |  |
| `zip_demo/archive_module.py` | Importing from ZIP archives (line 231) |  |
| `zip_demo/check.py` | Importing from ZIP archives (line 236) |  |
| `package_api/check_zip.py` | Importing from ZIP archives › The same package API inside a ZIP (line 269) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_try-it-yourself.py` | Try it yourself (line 362) | runs on its own |
