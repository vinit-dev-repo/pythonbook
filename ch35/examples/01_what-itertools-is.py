# Eager: builds a full list of 1,000,000 squares to select only five
squares = [n * n for n in range(1, 1_000_001)]
first_five = squares[:5]

# Lazy: itertools never computes a square you didn't ask for
import itertools
squares_lazy = (n * n for n in itertools.count(1))
first_five_lazy = list(itertools.islice(squares_lazy, 5))
print(first_five_lazy)
