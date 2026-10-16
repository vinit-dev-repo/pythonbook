import re

ordinary = "\bcat\b"
boundary = r"\bcat\b"
print(repr(ordinary))
print(re.search(ordinary, "a cat naps"))
print(re.search(boundary, "a cat naps").group())
print(re.fullmatch(ordinary, "\x08cat\x08") is not None)
