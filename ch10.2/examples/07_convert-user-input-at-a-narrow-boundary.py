for text in ("2.75", "-6e1", "not-a-number"):
    try:
        value = float(text)
    except ValueError:
        print("rejected:", text)
    else:
        print("accepted:", value)
