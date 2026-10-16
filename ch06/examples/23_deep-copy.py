import copy
shared = [1, 2]
src = [shared, shared]           # ONE list, listed twice
dup = copy.deepcopy(src)
print(dup[0] is dup[1])          # still one list, listed twice?
print(dup[0] is src[0])          # the same list as the original's?
