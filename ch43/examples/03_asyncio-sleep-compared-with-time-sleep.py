import time

def blocking_task(name):
    print(f"{name}: starting")
    time.sleep(3)               # blocks this thread for 3 seconds
    print(f"{name}: done")
