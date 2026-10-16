try:
    open("no-such-file.txt")
except FileNotFoundError as error:
    print("caught:", type(error).__name__)
    print("it is an OSError:", isinstance(error, OSError))
