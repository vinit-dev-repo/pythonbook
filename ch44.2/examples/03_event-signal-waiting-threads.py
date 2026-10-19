import threading
import time

start_signal = threading.Event()
finished = []
tally_lock = threading.Lock()

def runner(name):
    start_signal.wait()          # blocks here until set() is called
    with tally_lock:             # a shared list still needs a lock
        finished.append(name)

threads = [threading.Thread(target=runner, args=(f"Runner-{i}",)) for i in range(1, 4)]
for t in threads:
    t.start()

time.sleep(1)                    # let everyone line up
print(f"{len(threads)} runners are at the line, all blocked on .wait()")
print("BANG!")
start_signal.set()               # fires the starting gun for everyone at once

for t in threads:
    t.join()

print("every runner got past the gun:", sorted(finished))
