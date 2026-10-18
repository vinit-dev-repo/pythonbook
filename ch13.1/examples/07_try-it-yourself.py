import re

# 1
print(re.findall(r"\b[A-Z]\w*", "My Name is Vinit and I live in Delhi"))
# ['My', 'Name', 'Vinit', 'I', 'Delhi']

# 2
text = "42 apples"
print(re.match(r"\d+", text))        # a Match for '42'
print(re.search(r"\d+", text))       # a Match for '42'
print(re.fullmatch(r"\d+", text))    # None: the whole text is not digits

# 3
print(re.search(r"a.*b", "a123b456b").group())    # a123b456b  (greedy: goes to the LAST b)
print(re.search(r"a.*?b", "a123b456b").group())   # a123b     (lazy: stops at the FIRST b)

# 4
print(len("\bcat"), len(r"\bcat"))   # 4 5: a normal string turns \b into one backspace character
