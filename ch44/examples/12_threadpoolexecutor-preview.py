from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=3) as pool:
    results = pool.map(lambda n: n * n, [1, 2, 3, 4])
print(list(results))
