class UnavailableError(AppError):
    pass

try:
    raise UnavailableError("Try again later")
except AppError as error:
    print("Expected app failure:", error)
