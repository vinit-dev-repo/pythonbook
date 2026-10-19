# 1
import multiprocessing

def send_numbers(q):
    for i in range(1, 6):
        q.put(i)

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=send_numbers, args=(q,))
    p.start()
    # Read the number of items we KNOW were sent. Never loop on `q.empty()`:
    # the docs call it unreliable, because an item already handed over may not
    # have arrived in the queue yet, so `empty()` can say True and then be wrong.
    for _ in range(5):
        print(q.get())
    p.join()   # drain first, THEN join - a child can block waiting to hand over


# 2
def square_server(conn):
    number = conn.recv()
    conn.send(number * number)
    conn.close()


if __name__ == "__main__":
    parent_end, child_end = multiprocessing.Pipe()
    child = multiprocessing.Process(target=square_server, args=(child_end,))
    child.start()
    parent_end.send(7)
    print(parent_end.recv())
    child.join()


# 3
def add_many(counter, repeats):
    for _ in range(repeats):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    counter = multiprocessing.Value("i", 0)
    workers = [
        multiprocessing.Process(target=add_many, args=(counter, 1000))
        for _ in range(2)
    ]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    print(counter.value)
