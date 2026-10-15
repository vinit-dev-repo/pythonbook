# exercise_race.py
import threading
from race_schedule import lost_update
from locked_update import protected_update

assert lost_update(1000, 3) == 1003
assert protected_update(1000, 3) == 1006
print("controlled:", 1003, "protected:", 1006)

lock = threading.Lock()
total = 0

def read_total():
    return total

def write_total(new_value):
    global total
    total = new_value

# Splitting one update into two locked regions still loses an update.
# The barrier forces both threads to read 0 before either writes 1.
total = 0
both_read = threading.Barrier(2)

def split_update():
    with lock:
        current = read_total()
    both_read.wait(timeout=5)
    with lock:
        write_total(current + 1)

threads = [threading.Thread(target=split_update) for _ in range(2)]
for thread in threads: thread.start()
for thread in threads: thread.join()
print("separately locked read and write:", total)  # 1; two increments should give 2

assert total == 1
