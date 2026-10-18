numbers_iter = iter([5, 1, 9, 3])

print(min(numbers_iter))     # walks the ENTIRE iterator to find the minimum
print(max(numbers_iter))     # nothing left to walk -- ERROR!
