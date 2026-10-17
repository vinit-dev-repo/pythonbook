# 1
def power(base, exponent=2):
    return base ** exponent

print(power(3))       # 9
print(power(2, 5))    # 32

# 2
def add_score(score, scores=None):
    if scores is None:
        scores = []
    scores.append(score)
    return scores

print(add_score(10))   # [10]
print(add_score(20))   # [20]  -- not [10, 20], because it's a fresh list each time

# 3
# delivered_total(20) is 25 and delivered_total(20, shipping) is 32:
# the default is still the integer 5; the explicit call supplies the current 12.

# 4
# choose_colour(None) returns "no colour", choose_colour("") returns the empty string
# and choose_colour() returns "blue". Identity with the saved marker detects omission
# without treating every falsy value as missing.
