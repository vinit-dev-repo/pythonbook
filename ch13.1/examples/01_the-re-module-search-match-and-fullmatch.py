import re

text = "  hello world"

print(re.match(r"hello", text))       # fails: text doesn't START with "hello"
print(re.search(r"hello", text))      # succeeds: "hello" is IN there somewhere
print(re.fullmatch(r"hello", text))   # fails: the whole string isn't just "hello"
