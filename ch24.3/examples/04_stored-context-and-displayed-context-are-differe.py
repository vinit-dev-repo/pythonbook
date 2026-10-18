class AppError(Exception):
    pass

try:
    try:
        int("not a number")
    except ValueError:
        raise AppError("The setting is not a number") from None
except AppError as error:
    hidden_context = error.__context__
    explicit_cause = error.__cause__
    suppress_context = error.__suppress_context__
