import traceback

try:
    1 / 0
except ZeroDivisionError:
    print("carrying on, but here is what happened:")
    print(traceback.format_exc().strip())

print("still running")
