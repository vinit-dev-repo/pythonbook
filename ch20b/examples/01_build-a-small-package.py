def total_units(counts):
    if any(count < 0 for count in counts):
        raise ValueError("counts must be non-negative")
    return sum(counts)


def main():
    print(f"Units: {total_units([3, 5])}")


if __name__ == "__main__":
    main()
