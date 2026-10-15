# test_waiting.py
import pytest
from waiting import seconds_left

@pytest.mark.parametrize("now, expected", [(109, 1), (110, 0), (111, 0)])
def test_before_at_and_after_deadline(now, expected):
    assert seconds_left(started_at=100, now=now, wait=10) == expected
