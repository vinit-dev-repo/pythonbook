try:
    bad = {[1, 2]: "oops"}
except TypeError as e:
    print(e)
