# 1
# Windows starts new processes with "spawn", which re-imports the whole
# script fresh in the new process — without the __main__ guard, that
# re-import would try to start MORE processes, over and over.


# 2
import multiprocessing


def report(label):
    print(label, "running in a child process")


if __name__ == "__main__":
    child = multiprocessing.Process(target=report, args=("job-1",))
    child.start()
    child.join()
    print("exit code:", child.exitcode, flush=True)


# 3
def count_primes(limit):
    count = 0
    for n in range(2, limit):
        is_prime = True
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count


def show_count(limit):
    print(count_primes(limit))


if __name__ == "__main__":
    worker = multiprocessing.Process(target=show_count, args=(100,))
    worker.start()
    worker.join()
    print("done")
