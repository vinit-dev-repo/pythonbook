# 35 - The itertools Toolbox

The code of the chapter **35 - The itertools Toolbox** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What `itertools` provides, which tools read input immediately, and which tools produce output lazily
- How to select parts of an iterator without first creating a list
- How to stop the infinite iterators `count`, `cycle`, and `repeat`
- How to glue iterators together (`chain`) and copy one (`tee`)
- `starmap` and `accumulate` — mapping and running totals
- `zip_longest` and the `strict=True` safety net
- How `groupby` handles consecutive equal keys
- The four combinatorics tools: `product`, `permutations`, `combinations`, `combinations_with_replacement`

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_what-itertools-is.py` | What itertools is (line 49) | runs on its own |
| `examples/02_aggregators-recap-min-max-sum-any-all.py` | Aggregators recap: min, max, sum, any, all (line 95) | may use names from earlier examples |
| `examples/03_aggregators-recap-min-max-sum-any-all.py` | Aggregators recap: min, max, sum, any, all (line 109) | may use names from earlier examples |
| `examples/04_empty-input-and-the-state-left-after-a-reduction.py` | Empty input and the state left after a reduction (line 141) | runs on its own |
| `examples/05_slicing-an-iterator-islice.py` | Slicing an iterator: islice (line 184) | raises an error on purpose |
| `examples/06_slicing-an-iterator-islice.py` | Slicing an iterator: islice (line 200) | may use names from earlier examples |
| `examples/07_slicing-an-iterator-islice.py` | Slicing an iterator: islice (line 221) | may use names from earlier examples |
| `examples/08_filter-recap.py` | filter — recap (line 256) | may use names from earlier examples |
| `examples/09_filterfalse-the-opposite-of-filter.py` | filterfalse — the opposite of filter (line 271) | may use names from earlier examples |
| `examples/10_compress-pick-by-a-mask.py` | compress — pick by a mask (line 294) | may use names from earlier examples |
| `examples/11_takewhile-and-dropwhile.py` | takewhile and dropwhile (line 337) | may use names from earlier examples |
| `examples/12_count-a-lazy-counter.py` | count — a lazy counter (line 376) | may use names from earlier examples |
| `examples/13_count-a-lazy-counter.py` | count — a lazy counter (line 394) | may use names from earlier examples |
| `examples/14_cycle-repeat-a-sequence-forever.py` | cycle — repeat a sequence forever (line 419) | may use names from earlier examples |
| `examples/15_repeat-repeat-one-value.py` | repeat — repeat one value (line 449) | may use names from earlier examples |
| `examples/16_repeat-repeat-one-value.py` | repeat — repeat one value (line 466) | may use names from earlier examples |
| `examples/17_chain-glue-iterables-end-to-end.py` | chain — glue iterables end to end (line 492) | may use names from earlier examples |
| `examples/18_chain-from-iterable-when-you-already-have-a-list.py` | chain.from_iterable — when you already have a list of lists (line 511) | may use names from earlier examples |
| `examples/19_tee-n-independent-copies-of-one-iterator.py` | tee — N independent copies of one iterator (line 534) | may use names from earlier examples |
| `examples/20_map-recap.py` | map — recap (line 565) | may use names from earlier examples |
| `examples/21_starmap-map-that-unpacks-tuples-for-you.py` | starmap — map that unpacks tuples for you (line 582) | may use names from earlier examples |
| `examples/22_starmap-map-that-unpacks-tuples-for-you.py` | starmap — map that unpacks tuples for you (line 613) | may use names from earlier examples |
| `examples/23_accumulate-running-totals.py` | accumulate — running totals (line 638) | may use names from earlier examples |
| `examples/24_accumulate-running-totals.py` | accumulate — running totals (line 653) | may use names from earlier examples |
| `examples/25_accumulate-vs-functools-reduce.py` | accumulate vs functools.reduce (line 675) | may use names from earlier examples |
| `examples/26_zip-recap.py` | zip — recap (line 709) | may use names from earlier examples |
| `examples/27_zip-longest-keep-going-fill-the-gaps.py` | zip_longest — keep going, fill the gaps (line 726) | may use names from earlier examples |
| `examples/28_zip-strict-true-refuse-to-drop-anything-silently.py` | zip(..., strict=True) — refuse to drop anything silently (line 745) | raises an error on purpose |
| `examples/29_build-a-small-pairing-iterator.py` | Build a small pairing iterator (line 774) | may use names from earlier examples |
| `examples/30_build-a-small-pairing-iterator.py` | Build a small pairing iterator (line 814) | may use names from earlier examples |
| `examples/31_keep-unfinished-inputs-and-fill-exhausted-column.py` | Keep unfinished inputs and fill exhausted columns (line 836) | may use names from earlier examples |
| `examples/32_groupby-group-consecutive-equal-keys.py` | groupby — group CONSECUTIVE equal keys (line 888) | may use names from earlier examples |
| `examples/33_groupby-group-consecutive-equal-keys.py` | groupby — group CONSECUTIVE equal keys (line 916) | may use names from earlier examples |
| `examples/34_combinatorics-product-permutations-combinations.py` | Combinatorics: product, permutations, combinations (line 967) | may use names from earlier examples |
| `examples/35_product-nested-loops-in-one-call.py` | product — nested loops in one call (line 999) | may use names from earlier examples |
| `examples/36_product-nested-loops-in-one-call.py` | product — nested loops in one call (line 1021) | may use names from earlier examples |
| `examples/37_product-nested-loops-in-one-call.py` | product — nested loops in one call (line 1029) | may use names from earlier examples |
| `examples/38_permutations-order-matters.py` | permutations — order matters (line 1052) | may use names from earlier examples |
| `examples/39_permutations-order-matters.py` | permutations — order matters (line 1075) | may use names from earlier examples |
| `examples/40_combinations-order-does-not-matter.py` | combinations — order does not matter (line 1106) | may use names from earlier examples |
| `examples/41_combinations-with-replacement-groups-but-items-c.py` | combinations_with_replacement — groups, but items can repeat (line 1131) | may use names from earlier examples |
| `examples/42_adjacent-pairs-and-fixed-size-batches.py` | Adjacent pairs and fixed-size batches (line 1175) | runs on its own |
| `examples/43_observe-how-far-tools-consume-input.py` | Observe how far tools consume input (line 1223) | runs on its own |
| `examples/44_try-it-yourself.py` | Try it yourself (line 1319) | may use names from earlier examples |
