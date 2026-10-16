from functools import partial

print_csv = partial(print, sep=", ")   # stores ", " as the default; a call may override sep

print_csv("apple", "banana", "kiwi")
