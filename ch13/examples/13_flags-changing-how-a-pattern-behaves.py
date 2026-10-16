import re

pattern = re.compile(r"""
    ^                 # start of the string
    (\d{3})           # area code, 3 digits
    [-\s]             # a dash or whitespace
    (\d{4})           # the rest of the number, 4 digits
    $                 # end of the string
""", re.VERBOSE)

print(pattern.fullmatch("555-1234"))
print(pattern.fullmatch("555 1234"))
