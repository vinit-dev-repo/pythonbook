# crate_labels.py
"""Build concise labels for numbered storage crates."""


def label_for(number):
    """Return C- followed by a positive integer padded to at least four digits.

    Raises:
        TypeError: if number is not a built-in int.
        ValueError: if number is less than one.
    """
    if type(number) is not int:
        raise TypeError("number must be an int")
    if number < 1:
        raise ValueError("number must be positive")
    return f"C-{number:04d}"


class LabelBatch:
    """Keep a snapshot of valid crate numbers in their supplied order."""

    def __init__(self, numbers):
        """Validate each number with label_for and save the resulting labels."""
        self.labels = tuple(label_for(number) for number in numbers)

    def joined(self):
        """Return the labels separated by commas, or empty text for no labels."""
        return ",".join(self.labels)


if __name__ == "__main__":
    print(LabelBatch([8, 23]).joined())
