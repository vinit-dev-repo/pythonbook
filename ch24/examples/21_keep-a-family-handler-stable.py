try:
    try:
        raise NameError("a programming bug")
    except AppError:
        print("Expected app failure")
except NameError:
    print("NameError passed the AppError handler")
