import multiprocessing
import os

def greet(name, parent_pid):
    same = os.getpid() == parent_pid
    print(f"Hello {name}. Running in the same process as my parent? {same}")

if __name__ == "__main__":
    p = multiprocessing.Process(target=greet, args=("Vinit", os.getpid()))
    p.start()
    p.join()
