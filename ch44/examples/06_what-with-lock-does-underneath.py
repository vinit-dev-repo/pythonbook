lock.acquire()   # wait until the lock is available, then acquire it
try:
    current = read_balance()
    write_balance(current + 1)
finally:
    lock.release()   # release the lock even if an error happened
