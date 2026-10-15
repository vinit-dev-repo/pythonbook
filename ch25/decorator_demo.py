# decorator_demo.py
from boundaries import diagnosed


failure = ValueError("deliberate decorated failure")


@diagnosed
def choose(value, *, fail=False):
    """Return value unless this demonstration requests a failure."""
    if fail:
        raise failure
    return value


def main():
    print("returned:", choose(None))
    print("returned:", choose(42))
    try:
        choose("unused", fail=True)
    except ValueError as caught:
        print("same error:", caught is failure)
    print("name:", choose.__name__)


if __name__ == "__main__":
    main()
