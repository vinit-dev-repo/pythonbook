import multiprocessing

def worker(q):
    q.put("result from the worker process")

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=worker, args=(q,))
    p.start()
    print(q.get())     # blocks until something is put in
    p.join()
