import threading

# 3
names = []
lock = threading.Lock()


def record():
    with lock:
        names.append(threading.current_thread().name)


threads = [threading.Thread(target=record, name=f"Worker-{i}") for i in range(1, 4)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(sorted(names))
