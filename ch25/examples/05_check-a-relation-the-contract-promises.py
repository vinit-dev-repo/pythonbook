def test_average_of_reordered_small_integers():
    assert average([2, 4, 6]) == 4
    assert average([6, 2, 4]) == 4
