# test_triple.py
def triple(x):
    return x * 2                # the bug

def test_triple_runs():
    triple(4)                   # no assertion

def test_triple_result():
    assert triple(4) == 12
