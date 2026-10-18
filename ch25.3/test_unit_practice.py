# test_unit_practice.py
import unittest

def safe_sqrt(n):
    if n < 0:
        raise ValueError("cannot take the square root of a negative number")
    return n ** 0.5

class TestSafeSqrt(unittest.TestCase):
    def test_happy_path(self):
        self.assertEqual(safe_sqrt(9), 3)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            safe_sqrt(-4)

if __name__ == "__main__":
    unittest.main()
