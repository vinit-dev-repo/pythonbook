# 35 - The itertools Toolbox

The code of this chapter of the Python tutorial, extracted byte for byte from the certified chapter. The chapter explains every line; read it there.

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Section | Note |
|---|---|---|
| `examples/01_what-itertools-is.py` | What itertools is | runs on its own |
| `examples/02_aggregators-recap-min-max-sum-any-all.py` | Aggregators recap: min, max, sum, any, all | may use names from earlier examples |
| `examples/03_aggregators-recap-min-max-sum-any-all.py` | Aggregators recap: min, max, sum, any, all | may use names from earlier examples |
| `examples/04_empty-input-and-the-state-left-after-a-reduction.py` | Empty input and the state left after a reduction | runs on its own |
| `examples/05_slicing-an-iterator-islice.py` | Slicing an iterator: islice | raises an error on purpose |
| `examples/06_slicing-an-iterator-islice.py` | Slicing an iterator: islice | may use names from earlier examples |
| `examples/07_slicing-an-iterator-islice.py` | Slicing an iterator: islice | may use names from earlier examples |
| `examples/08_filter-recap.py` | filter — recap | may use names from earlier examples |
| `examples/09_filterfalse-the-opposite-of-filter.py` | filterfalse — the opposite of filter | may use names from earlier examples |
| `examples/10_compress-pick-by-a-mask.py` | compress — pick by a mask | may use names from earlier examples |
| `examples/11_takewhile-and-dropwhile.py` | takewhile and dropwhile | may use names from earlier examples |
| `examples/12_count-a-lazy-counter.py` | count — a lazy counter | may use names from earlier examples |
| `examples/13_count-a-lazy-counter.py` | count — a lazy counter | may use names from earlier examples |
| `examples/14_cycle-repeat-a-sequence-forever.py` | cycle — repeat a sequence forever | may use names from earlier examples |
| `examples/15_repeat-repeat-one-value.py` | repeat — repeat one value | may use names from earlier examples |
| `examples/16_repeat-repeat-one-value.py` | repeat — repeat one value | may use names from earlier examples |
| `examples/17_chain-glue-iterables-end-to-end.py` | chain — glue iterables end to end | may use names from earlier examples |
| `examples/18_chain-from-iterable-when-you-already-have-a-list.py` | chain.from_iterable — when you already have a list of lists | may use names from earlier examples |
| `examples/19_tee-n-independent-copies-of-one-iterator.py` | tee — N independent copies of one iterator | may use names from earlier examples |
| `examples/20_map-recap.py` | map — recap | may use names from earlier examples |
| `examples/21_starmap-map-that-unpacks-tuples-for-you.py` | starmap — map that unpacks tuples for you | may use names from earlier examples |
| `examples/22_starmap-map-that-unpacks-tuples-for-you.py` | starmap — map that unpacks tuples for you | may use names from earlier examples |
| `examples/23_accumulate-running-totals.py` | accumulate — running totals | may use names from earlier examples |
| `examples/24_accumulate-running-totals.py` | accumulate — running totals | may use names from earlier examples |
| `examples/25_accumulate-vs-functools-reduce.py` | accumulate vs functools.reduce | may use names from earlier examples |
| `examples/26_zip-recap.py` | zip — recap | may use names from earlier examples |
| `examples/27_zip-longest-keep-going-fill-the-gaps.py` | zip_longest — keep going, fill the gaps | may use names from earlier examples |
| `examples/28_zip-strict-true-refuse-to-drop-anything-silently.py` | zip(..., strict=True) — refuse to drop anything silently | raises an error on purpose |
| `examples/29_build-a-small-pairing-iterator.py` | Build a small pairing iterator | may use names from earlier examples |
| `examples/30_build-a-small-pairing-iterator.py` | Build a small pairing iterator | may use names from earlier examples |
| `examples/31_keep-unfinished-inputs-and-fill-exhausted-column.py` | Keep unfinished inputs and fill exhausted columns | may use names from earlier examples |
| `examples/32_groupby-group-consecutive-equal-keys.py` | groupby — group CONSECUTIVE equal keys | may use names from earlier examples |
| `examples/33_groupby-group-consecutive-equal-keys.py` | groupby — group CONSECUTIVE equal keys | may use names from earlier examples |
| `examples/34_combinatorics-product-permutations-combinations.py` | Combinatorics: product, permutations, combinations | may use names from earlier examples |
| `examples/35_product-nested-loops-in-one-call.py` | product — nested loops in one call | may use names from earlier examples |
| `examples/36_product-nested-loops-in-one-call.py` | product — nested loops in one call | may use names from earlier examples |
| `examples/37_product-nested-loops-in-one-call.py` | product — nested loops in one call | may use names from earlier examples |
| `examples/38_permutations-order-matters.py` | permutations — order matters | may use names from earlier examples |
| `examples/39_permutations-order-matters.py` | permutations — order matters | may use names from earlier examples |
| `examples/40_combinations-order-does-not-matter.py` | combinations — order does not matter | may use names from earlier examples |
| `examples/41_combinations-with-replacement-groups-but-items-c.py` | combinations_with_replacement — groups, but items can repeat | may use names from earlier examples |
| `examples/42_adjacent-pairs-and-fixed-size-batches.py` | Adjacent pairs and fixed-size batches | runs on its own |
| `examples/43_observe-how-far-tools-consume-input.py` | Observe how far tools consume input | runs on its own |
| `examples/44_try-it-yourself.py` | Try it yourself | may use names from earlier examples |
