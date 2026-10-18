def read_count(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(read_count("12"))
print(read_count("not a count"))
