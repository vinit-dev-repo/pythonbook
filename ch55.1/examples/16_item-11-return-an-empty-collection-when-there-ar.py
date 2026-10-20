try:
    for name in find_matches_bad(candidates, "Z"):
        print(name)
except TypeError as e:
    print("caller crashes:", e)
