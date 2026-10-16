def find_matches_bad(candidates, prefix):
    matches = [c for c in candidates if c.startswith(prefix)]
    return matches if matches else None   # returns None when nothing matches

def find_matches_good(candidates, prefix):
    return [c for c in candidates if c.startswith(prefix)]   # always a list, even an empty one

candidates = ["Ana", "Ben", "Cy"]

for name in find_matches_good(candidates, "Z"):
    print(name)
print("search finished")
