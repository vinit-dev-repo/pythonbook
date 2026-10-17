# 1
text = "  Hello, World!  "
print(text.strip().upper())              # HELLO, WORLD!

# 2
items = "apple,bread,milk".split(",")
print(items)                             # ['apple', 'bread', 'milk']
print("-".join(items))                   # apple-bread-milk

# 3
print("report.txt".removesuffix(".txt"))   # report
print("report.txt".rstrip(".txt"))         # repor: rstrip removes any of the characters

# 4
word = "cat"
new_word = "b" + word[1:]
print(word)                              # cat
print(new_word)                          # bat
