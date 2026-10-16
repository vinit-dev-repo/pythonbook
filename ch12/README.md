# 12 - The Standard Library Tour

The code of the chapter **12 - The Standard Library Tour** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- `time` — timestamps and pausing the current thread
- `datetime` — dates, times, formatting and parsing
- Date arithmetic, and the difference between a "naive" and an "aware" datetime
- `csv` — reading and writing spreadsheet-style files
- `random` — randomness, and why a "seed" makes randomness repeatable
- `math` — the everyday maths functions beyond `+ - * /`
- `statistics` — mean, median, mode and spread, without doing the sums yourself
- `bisect`, packed array files, and bounded deque operations
- `decimal` — exact decimal inputs and explicit rounding
- Forwarding a function call through a timing helper without changing its returned result
- `annotationlib` — when annotations are evaluated and how that differs from type checking
- Template strings — capturing values separately from text and processing them for a specific purpose
- Reusable brace and percent formats, numeric layouts, and dollar templates

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `schedule_search.py` | Search a schedule with gaps (line 732) |  |
| `keyed_insert.py` | Insert records and restrict a search range (line 777) |  |
| `packed_values.py` | `array` — save and reopen packed values (line 808) |  |
| `recent_events.py` | `deque` — bounded history and rotation (line 868) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_time-timestamps-and-pausing.py` | `time` — timestamps and pausing (line 63) | runs on its own |
| `examples/02_application-a-simple-function-timer.py` | Application: a simple function timer (line 97) | may use names from earlier examples |
| `examples/03_application-a-simple-function-timer.py` | Application: a simple function timer (line 117) | may use names from earlier examples |
| `examples/04_datetime-dates-times-and-formatting.py` | `datetime` — dates, times and formatting (line 150) | may use names from earlier examples |
| `examples/05_datetime-dates-times-and-formatting.py` | `datetime` — dates, times and formatting (line 171) | may use names from earlier examples |
| `examples/06_formatting-with-strftime.py` | Formatting with `strftime` (line 187) | may use names from earlier examples |
| `examples/07_parsing-with-strptime.py` | Parsing with `strptime` (line 227) | may use names from earlier examples |
| `examples/08_date-arithmetic-timedelta.py` | Date arithmetic: `timedelta` (line 259) | may use names from earlier examples |
| `examples/09_naive-and-aware-datetimes.py` | Naive and aware datetimes (line 289) | may use names from earlier examples |
| `examples/10_making-the-file-to-work-with.py` | Making the file to work with (line 339) | may use names from earlier examples |
| `examples/11_reading.py` | Reading (line 359) | may use names from earlier examples |
| `examples/12_reading.py` | Reading (line 381) | may use names from earlier examples |
| `examples/13_writing.py` | Writing (line 398) | may use names from earlier examples |
| `examples/14_dialects-quoting-and-records-that-span-lines.py` | Dialects, quoting and records that span lines (line 431) | may use names from earlier examples |
| `examples/15_random-controlled-randomness.py` | `random` — controlled randomness (line 480) | may use names from earlier examples |
| `examples/16_replacement-and-equal-values.py` | Replacement and equal values (line 519) | may use names from earlier examples |
| `examples/17_seeds-same-seed-same-random.py` | Seeds: same seed, same "random" (line 551) | may use names from earlier examples |
| `examples/18_timeit-measuring-which-version-is-faster.py` | `timeit` — measuring which version is faster (line 582) | may use names from earlier examples |
| `examples/19_timeit-measuring-which-version-is-faster.py` | `timeit` — measuring which version is faster (line 597) | may use names from earlier examples |
| `examples/20_math-everyday-maths-functions.py` | `math` — everyday maths functions (line 648) | may use names from earlier examples |
| `examples/21_bisect-keeping-a-list-sorted-without-re-sorting.py` | `bisect` — keeping a list sorted without re-sorting it (line 681) | may use names from earlier examples |
| `examples/22_bisect-keeping-a-list-sorted-without-re-sorting.py` | `bisect` — keeping a list sorted without re-sorting it (line 705) | may use names from earlier examples |
| `examples/23_statistics-summarising-numbers.py` | `statistics` — summarising numbers (line 919) | may use names from earlier examples |
| `examples/24_decimal-exact-numbers-for-money.py` | `decimal` — exact numbers for money (line 950) | may use names from earlier examples |
| `examples/25_decimal-exact-numbers-for-money.py` | `decimal` — exact numbers for money (line 967) | may use names from earlier examples |
| `examples/26_decimal-exact-numbers-for-money.py` | `decimal` — exact numbers for money (line 981) | may use names from earlier examples |
| `examples/27_when-annotations-are-evaluated-3-14-changed-this.py` | When annotations are evaluated (3.14 changed this) (line 1019) | may use names from earlier examples |
| `examples/28_when-annotations-are-evaluated-3-14-changed-this.py` | When annotations are evaluated (3.14 changed this) (line 1028) | may use names from earlier examples |
| `examples/29_when-annotations-are-evaluated-3-14-changed-this.py` | When annotations are evaluated (3.14 changed this) (line 1046) | may use names from earlier examples |
| `examples/30_t-strings-keep-text-and-values-separate-3-14.py` | t-strings keep text and values separate (3.14+) (line 1082) | may use names from earlier examples |
| `examples/31_t-strings-keep-text-and-values-separate-3-14.py` | t-strings keep text and values separate (3.14+) (line 1101) | may use names from earlier examples |
| `examples/32_walking-a-template.py` | Walking a template (line 1129) | may use names from earlier examples |
| `examples/33_escaping-a-value-used-as-html-text.py` | Escaping a value used as HTML text (line 1158) | may use names from earlier examples |
| `examples/34_two-details-that-catch-people-out.py` | Two details that catch people out (line 1192) | may use names from earlier examples |
| `examples/35_two-details-that-catch-people-out.py` | Two details that catch people out (line 1210) | may use names from earlier examples |
| `examples/36_two-details-that-catch-people-out.py` | Two details that catch people out (line 1234) | may use names from earlier examples |
| `examples/37_fill-a-saved-layout-with-later-values.py` | Fill a saved layout with later values (line 1280) | may use names from earlier examples |
| `examples/38_fill-a-saved-layout-with-later-values.py` | Fill a saved layout with later values (line 1304) | may use names from earlier examples |
| `examples/39_choose-a-width-sign-precision-and-base.py` | Choose a width, sign, precision and base (line 1326) | may use names from earlier examples |
| `examples/40_choose-a-width-sign-precision-and-base.py` | Choose a width, sign, precision and base (line 1355) | may use names from earlier examples |
| `examples/41_read-and-maintain-percent-formats.py` | Read and maintain percent formats (line 1375) | may use names from earlier examples |
| `examples/42_dollar-templates-use-a-different-template-class.py` | Dollar templates use a different Template class (line 1405) | may use names from earlier examples |
| `examples/43_a-quote-mark-and-a-space-have-different-jobs.py` | A quote mark and a space have different jobs (line 1443) | runs on its own |
| `examples/44_model-parameters-are-not-a-sample-s-measured-sum.py` | Model parameters are not a sample's measured summary (line 1482) | runs on its own |
| `examples/45_try-it-yourself.py` | Try it yourself (line 1557) | may use names from earlier examples |
