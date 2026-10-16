import multiprocessing

def add(a, b):
    return a + b

if __name__ == "__main__":
    with multiprocessing.Pool(4) as pool:
        print(pool.starmap(add, [(1, 2), (3, 4), (5, 6)]))
