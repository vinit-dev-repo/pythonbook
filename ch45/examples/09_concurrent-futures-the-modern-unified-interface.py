from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def square(n):
    return n * n

if __name__ == "__main__":
    # I/O-bound work -> ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=4) as pool:
        print(list(pool.map(square, [1, 2, 3, 4])))

    # CPU-bound work -> ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=4) as pool:
        print(list(pool.map(square, [1, 2, 3, 4])))
