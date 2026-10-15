import pytest
from shop_report.cli import main, total_units


def test_total_and_empty_list():
    assert total_units([3, 5]) == 8
    assert total_units([]) == 0


def test_negative_count_is_rejected():
    with pytest.raises(ValueError, match="non-negative"):
        total_units([3, -1])


def test_command_output(capsys):
    main()
    assert capsys.readouterr().out == "Units: 8\n"
