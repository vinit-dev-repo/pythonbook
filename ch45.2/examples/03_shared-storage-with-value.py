import multiprocessing

def add_many(counter, repeats):
    for _ in range(repeats):
        with counter.get_lock():
            counter.value += 1

if __name__ == "__main__":
    counter = multiprocessing.Value("i", 0)
    workers = [
        multiprocessing.Process(target=add_many, args=(counter, 10_000))
        for _ in range(4)
    ]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    print(counter.value)
