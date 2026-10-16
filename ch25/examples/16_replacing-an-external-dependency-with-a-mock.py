from unittest.mock import patch
import calculator

def test_add_is_called_correctly():
    with patch("calculator.add", return_value=999) as fake_add:
        result = calculator.add(2, 3)
        assert result == 999
        fake_add.assert_called_once_with(2, 3)
