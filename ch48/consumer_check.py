# consumer_check.py
from pathlib import Path
import sys

import shop_report
from shop_report.cli import total_units


def main():
    origin = Path(shop_report.__file__).resolve()
    assert origin.is_relative_to(Path(sys.prefix).resolve())
    assert total_units([4, 0, 6]) == 10
    assert total_units([]) == 0
    try:
        total_units([4, -1, 6])
    except ValueError as error:
        assert str(error) == "counts must be non-negative"
    else:
        raise AssertionError("negative count was accepted")
    print("installed wheel: new inputs and package origin pass")


if __name__ == "__main__":
    main()
