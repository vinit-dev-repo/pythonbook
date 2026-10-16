import threading
import time

semaphore = threading.Semaphore(3)   # only 3 "parking spaces"

def download(name):
    with semaphore:
        print(f"{name}: downloading...")
        time.sleep(1)
        print(f"{name}: done")

names = [f"file{i}" for i in range(1, 6)]
threads = [threading.Thread(target=download, args=(n,)) for n in names]
for t in threads:
    t.start()
for t in threads:
    t.join()
