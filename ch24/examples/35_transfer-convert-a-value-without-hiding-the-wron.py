for value in ("TrUe", 2, " true "):
    try:
        print(repr(value), "->", convert_bool(value))
    except ConversionError as error:
        print(repr(value), "->", type(error.__cause__).__name__,
              str(error.__cause__))
