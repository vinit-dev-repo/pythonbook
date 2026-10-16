class AppError(Exception):
    pass

for error in (AppError(), AppError("Try again"), AppError("bad item", 7)):
    print(error.args, repr(str(error)))
