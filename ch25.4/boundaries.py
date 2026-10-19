# boundaries.py
import traceback
from functools import wraps


def safe_call(callee, *args, **kwargs):
    try:
        return True, callee(*args, **kwargs)
    except Exception as error:
        traceback.print_exception(error)
        return False, error


def diagnosed(callee):
    @wraps(callee)
    def wrapper(*args, **kwargs):
        try:
            return callee(*args, **kwargs)
        except Exception as error:
            traceback.print_exception(error)
            raise
    return wrapper
