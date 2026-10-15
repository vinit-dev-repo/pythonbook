# hash_bits_lab.py
import sys

width = sys.hash_info.width
mask = (1 << width) - 1
def differing_bits(left, right):
    return ((hash(left) & mask) ^ (hash(right) & mask)).bit_count()

print("hash width:", width)
for left, right in [(2, 2.0), (2.0, 2.125),
                    (17, 17 + sys.hash_info.modulus)]:
    first = hash(left) & mask
    second = hash(right) & mask
    print("bits:", format(first, f"0{width}b"), format(second, f"0{width}b"))
    print("equal values:", left == right, "different bits:", differing_bits(left, right))
assert differing_bits(2, 2.0) == 0
assert hash(17) == hash(17 + sys.hash_info.modulus)
