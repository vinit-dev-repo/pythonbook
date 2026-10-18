import re

digit_pattern = re.compile(r"\d+")

print(digit_pattern.findall("3 cats and 12 dogs"))
print(digit_pattern.findall("100 sheep"))
