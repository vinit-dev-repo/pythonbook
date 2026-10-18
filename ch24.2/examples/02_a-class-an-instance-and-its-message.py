problem = AppError("Try again")
try:
    raise problem
except AppError as error:
    same_object = error is problem
