# cli_demo/labels.py
"""Reusable labels plus an optional command-line interface."""
import argparse

def make_label(text, count=1):
    """Return count uppercase copies separated by spaces."""
    if isinstance(count, bool) or not isinstance(count, int):
        raise TypeError("count must be an integer, not bool")
    if count < 1:
        raise ValueError("count must be positive")
    return " ".join([text.upper()] * count)

def self_test():
    assert make_label("go", 2) == "GO GO"
    assert make_label("hi") == "HI"

def main(argv=None):
    parser = argparse.ArgumentParser(description="Build an uppercase label.")
    parser.add_argument("text", help="text to display")
    parser.add_argument("--count", type=int, default=1, help="positive repetition count")
    args = parser.parse_args(argv)
    if args.count < 1:
        parser.error("--count must be positive")
    print(make_label(args.text, args.count))

if __name__ == "__main__":
    self_test()
    main()
