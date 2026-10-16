def build_concat(n):
    s = ""
    for i in range(n):
        s += str(i)         # looks like the trap - but see below
    return s

def build_join(n):
    return "".join(str(i) for i in range(n))   # each piece copied exactly once

def build_concat_kept(n):
    s = ""
    history = []
    for i in range(n):
        s += str(i)
        history.append(s)   # a second name now points at the string
    return s

for builder in (build_concat, build_join, build_concat_kept):
    assert builder(0) == ""
    assert builder(1) == "0"
    assert builder(10) == "0123456789"
assert build_concat(100) == build_join(100) == build_concat_kept(100)
print("builder checks passed")
