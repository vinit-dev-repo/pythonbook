import time

start = time.perf_counter()
print("Working...")
time.sleep(1)          # request a 1-second pause in this thread
end = time.perf_counter()

elapsed = end - start
print(f"That took about {elapsed:.1f} seconds")
