import bisect

scores = [10, 20, 30, 40, 50]
print(bisect.bisect_left(scores, 30))
print(bisect.bisect_right(scores, 30))
print(bisect.bisect_left(scores, 35))
