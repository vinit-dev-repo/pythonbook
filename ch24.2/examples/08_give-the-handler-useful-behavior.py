try:
    raise FormatFailure
except TypeError:
    print("The required constructor arguments were missing")
