# 1
class Found(Exception):
    pass

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
try:
    for row_no, row in enumerate(grid):
        for col_no, value in enumerate(row):
            if value == 8:
                raise Found((row_no, col_no))
except Found as hit:
    print("found 8 at", hit.args[0])      # found 8 at (2, 1)

# 2
# Both 3.5 and later fail integer conversion, so the message prints twice;
# the third prompt accepts 42 and the last line is: Entered: 42

# 3
prices = {"milk": 1.50}
if "bread" in prices:                       # LBYL: look first
    print(prices["bread"])
else:
    print("No price for bread")

try:                                        # EAFP: try first
    print(prices["bread"])
except KeyError:
    print("No price for bread")
