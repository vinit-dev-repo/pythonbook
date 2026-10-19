import multiprocessing

def worker(conn):
    conn.send("hello from the child")
    conn.close()

if __name__ == "__main__":
    parent_end, child_end = multiprocessing.Pipe()
    p = multiprocessing.Process(target=worker, args=(child_end,))
    p.start()
    print(parent_end.recv())
    p.join()
