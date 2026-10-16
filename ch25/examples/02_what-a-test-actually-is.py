def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

test_add()
print("test passed, no output means the assert was fine")
