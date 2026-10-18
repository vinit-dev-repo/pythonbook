def safe_call(callee, *args):
    try:
        return True, callee(*args)
    except Exception as error:
        return False, error

print(safe_call(int, "12"))                    # (True, 12)
ok, error = safe_call(int, "x")
print(ok, type(error).__name__)                # False ValueError
print(safe_call(lambda: None))                 # (True, None)
