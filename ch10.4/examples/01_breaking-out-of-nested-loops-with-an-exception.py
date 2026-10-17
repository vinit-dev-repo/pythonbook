class Found(Exception):
    """Raised to jump out of every loop at once."""

grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

try:
    for row_no, row in enumerate(grid):
        for col_no, value in enumerate(row):
            if value == 5:
                raise Found((row_no, col_no))
except Found as hit:
    print("found 5 at", hit.args[0])
else:
    print("5 is not in the grid")
