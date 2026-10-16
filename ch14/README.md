# 14 - Text, Bytes and Encodings

The code of the chapter **14 - Text, Bytes and Encodings** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What a character really is, and the difference between a **code point** and a **byte**
- The `bytes` and `bytearray` types, and byte literals like `b"..."`
- `.encode()` and `.decode()` — turning text into bytes, and bytes back into text
- The encodings you will meet the most: UTF-8, UTF-16, Latin-1, cp1252, ASCII
- `UnicodeEncodeError` and `UnicodeDecodeError` — what each one really means
- The `errors=` handlers that control what happens when a character will not fit
- The "Unicode sandwich" — a design that keeps text and bytes separate
- Opening files with `encoding=`, and why defaults differ between systems
- The BOM, and the `utf-8-sig` encoding built to handle it
- Unicode normalisation and case folding under an explicit comparison policy
- `memoryview` — reading a slice of bytes without copying it
- Code-point sorting, limited search aliases, locale collation and versioned Unicode sort keys
- Inspecting distinct encoding settings and treating encoding detection as a hypothesis
- Binary field layouts, line-ending policies and standard-stream settings

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `binary_operations.py` | The bytes and bytearray types › Binary methods can copy or mutate (line 227) |  |
| `literal_encodings.py` | Python source files have an encoding › A literal, a display and encoded text are different (line 502) |  |
| `text_file_boundaries.py` | Reading and writing files with encoding= › Text mode also translates line endings (line 667) |  |
| `utf16_streams.py` | The BOM and utf-8-sig › UTF-16 streams need a byte-order rule (line 830) |  |
| `cast_buffer.py` | memoryview: reading bytes without copying them › Cast a view and release the buffer (line 1197) |  |
| `packed_record.py` | Pack a record with an explicit binary layout (line 1261) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_what-a-character-really-is.py` | What a character really is (line 76) | runs on its own |
| `examples/02_what-a-character-really-is.py` | What a character really is (line 101) | may use names from earlier examples |
| `examples/03_the-bytes-and-bytearray-types.py` | The bytes and bytearray types (line 141) | may use names from earlier examples |
| `examples/04_the-bytes-and-bytearray-types.py` | The bytes and bytearray types (line 163) | may use names from earlier examples |
| `examples/05_constructing-binary-data-deliberately.py` | The bytes and bytearray types › Constructing binary data deliberately (line 197) | may use names from earlier examples |
| `examples/06_why-printing-bytes-looks-like-a-mix-of-text-and.py` | The bytes and bytearray types › Why printing bytes looks like a mix of text and code (line 273) | may use names from earlier examples |
| `examples/07_encode-and-decode-the-two-directions.py` | encode() and decode(): the two directions (line 295) | may use names from earlier examples |
| `examples/08_unicodeencodeerror-and-unicodedecodeerror.py` | UnicodeEncodeError and UnicodeDecodeError (line 337) | may use names from earlier examples |
| `examples/09_unicodeencodeerror-and-unicodedecodeerror.py` | UnicodeEncodeError and UnicodeDecodeError (line 353) | may use names from earlier examples |
| `examples/10_unicodeencodeerror-and-unicodedecodeerror.py` | UnicodeEncodeError and UnicodeDecodeError (line 369) | may use names from earlier examples |
| `examples/11_the-errors-handlers.py` | The errors= handlers (line 412) | may use names from earlier examples |
| `examples/12_the-errors-handlers.py` | The errors= handlers (line 441) | may use names from earlier examples |
| `examples/13_python-source-files-have-an-encoding.py` | Python source files have an encoding (line 469) | runs on its own |
| `examples/14_bytes-do-not-reveal-their-encoding.py` | Bytes do not reveal their encoding (line 542) | runs on its own |
| `examples/15_a-detector-proposes-an-interpretation.py` | Bytes do not reveal their encoding › A detector proposes an interpretation (line 570) | may use names from earlier examples |
| `examples/16_reading-and-writing-files-with-encoding.py` | Reading and writing files with encoding= (line 614) | may use names from earlier examples |
| `examples/17_reading-and-writing-files-with-encoding.py` | Reading and writing files with encoding= (line 636) | may use names from earlier examples |
| `examples/18_inspect-the-encoding-used-at-each-boundary.py` | Reading and writing files with encoding= › Inspect the encoding used at each boundary (line 721) | may use names from earlier examples |
| `examples/19_the-bom-and-utf-8-sig.py` | The BOM and utf-8-sig (line 778) | may use names from earlier examples |
| `examples/20_the-bom-and-utf-8-sig.py` | The BOM and utf-8-sig (line 792) | may use names from earlier examples |
| `examples/21_unicode-normalisation.py` | Unicode normalisation (line 877) | may use names from earlier examples |
| `examples/22_unicode-normalisation.py` | Unicode normalisation (line 916) | may use names from earlier examples |
| `examples/23_some-apis-preserve-str-or-bytes.py` | Some APIs preserve `str` or `bytes` (line 948) | runs on its own |
| `examples/24_regex-has-a-text-form-and-a-bytes-form.py` | Regex has a text form and a bytes form (line 983) | runs on its own |
| `examples/25_case-folding.py` | Case folding (line 1012) | may use names from earlier examples |
| `examples/26_case-folding.py` | Case folding (line 1033) | may use names from earlier examples |
| `examples/27_looking-up-unicode-character-data.py` | Looking up Unicode character data (line 1084) | runs on its own |
| `examples/28_numeric-characters-are-not-all-decimal-digits.py` | Looking up Unicode character data › Numeric characters are not all decimal digits (line 1104) | may use names from earlier examples |
| `examples/29_memoryview-reading-bytes-without-copying-them.py` | memoryview: reading bytes without copying them (line 1136) | may use names from earlier examples |
| `examples/30_memoryview-reading-bytes-without-copying-them.py` | memoryview: reading bytes without copying them (line 1170) | may use names from earlier examples |
| `examples/31_sorting-non-ascii-text.py` | Sorting non-ASCII text (line 1314) | may use names from earlier examples |
| `examples/32_sorting-non-ascii-text.py` | Sorting non-ASCII text (line 1328) | may use names from earlier examples |
| `examples/33_build-a-limited-search-alias-and-retain-the-orig.py` | Sorting non-ASCII text › Build a limited search alias and retain the original (line 1360) | may use names from earlier examples |
| `examples/34_locale-collation-uses-installed-system-rules.py` | Sorting non-ASCII text › Locale collation uses installed system rules (line 1407) | may use names from earlier examples |
| `examples/35_a-unicode-collation-key-has-a-data-version.py` | Sorting non-ASCII text › A Unicode collation key has a data version (line 1434) | may use names from earlier examples |
| `examples/36_try-it-yourself.py` | Try it yourself (line 1485) | may use names from earlier examples |

## Terminal commands

| File | Where it is in the chapter | Note |
|---|---|---|
| `commands/01_set-a-redirected-stream-s-encoding-before-launch.ps1` | Reading and writing files with encoding= › Set a redirected stream's encoding before launch (line 750) | powershell commands to type in a terminal |
