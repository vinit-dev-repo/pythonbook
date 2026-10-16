try:
    int("bad count")
except ValueError as conversion:
    try:
        {}["count"]
    except KeyError:
        try:
            raise RuntimeError("Cannot load count") from conversion
        except RuntimeError as error:
            print("Chosen cause:", type(error.__cause__).__name__)
            print("Current context:", type(error.__context__).__name__)
            print("Automatic context display suppressed:", error.__suppress_context__)
