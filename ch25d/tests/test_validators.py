# tests/test_validators.py
import pytest

from app.utils.validators import validate_integer, validate_text


class IntChild(int):
    pass


class StrChild(str):
    pass


@pytest.mark.parametrize("value", [True, 1.0, '1', None, IntChild(1)])
def test_integer_requires_the_exact_builtin_type(value):
    with pytest.raises(TypeError, match='count must be an int'):
        validate_integer('count', value)


@pytest.mark.parametrize("value, lower, upper", [
    (-100, None, None), (0, 0, 0), (1000, 1000, 50000), (50000, 1000, 50000),
    (2, None, 2), (-2, -2, None),
])
def test_success_and_inclusive_optional_bounds(value, lower, upper):
    assert validate_integer('count', value, lower, upper) is None


@pytest.mark.parametrize("value, lower, upper, message", [
    (-1, 0, None, 'count must be at least 0'),
    (1, None, 0, 'count must be at most 0'),
    (999, 1000, 50000, 'count must be at least 1000'),
    (50001, 1000, 50000, 'count must be at most 50000'),
    (1, 1, 0, 'count must be at most 0'),
])
def test_out_of_bounds_and_no_positive_quantity(value, lower, upper, message):
    with pytest.raises(ValueError) as error:
        validate_integer('count', value, lower, upper)
    assert str(error.value) == message


@pytest.mark.parametrize("side, message", [('lower', ''), ('upper', ''), ('lower', 'too few'), ('upper', 'too many')])
def test_custom_messages_including_empty_strings(side, message):
    with pytest.raises(ValueError) as error:
        if side == 'lower':
            validate_integer('count', -1, min_value=0, custom_min_message=message)
        else:
            validate_integer('count', 1, max_value=0, custom_max_message=message)
    assert str(error.value) == message


def test_text_normalization():
    assert validate_text('name', '  Router  ') == 'Router'


@pytest.mark.parametrize("value, error", [(None, TypeError), (1, TypeError),
                                        (StrChild('R'), TypeError), ('', ValueError), ('  ', ValueError)])
def test_text_rejections(value, error):
    with pytest.raises(error):
        validate_text('name', value)
