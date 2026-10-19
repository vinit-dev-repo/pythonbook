import time

big_list = list(range(1_000_000))
big_set = set(big_list)

start = time.perf_counter()
list_found = 999_999 in big_list
list_time = time.perf_counter() - start

start = time.perf_counter()
set_found = 999_999 in big_set
set_time = time.perf_counter() - start

assert list_found is True and set_found is True
assert 1_000_000 not in big_list and 1_000_000 not in big_set
print("both found the item:", list_found and set_found)
print(f"list lookup: {list_time:.9f} seconds")
print(f"set lookup: {set_time:.9f} seconds")
