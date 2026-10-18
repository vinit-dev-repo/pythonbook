# test_selection.py
from selection import positive_values

def test_mixed_values_keep_order_and_repeated_matches():
    values = [-2, 3, 0, 5, 3, 7]
    assert positive_values(values) == [3, 5, 3, 7]
    assert values == [-2, 3, 0, 5, 3, 7]
