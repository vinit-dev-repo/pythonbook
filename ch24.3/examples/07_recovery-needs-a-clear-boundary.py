def read_count_bad(text):
    try:
        return int(missing_count_text)
    except Exception:
        return 0

print(read_count_bad("12"))
