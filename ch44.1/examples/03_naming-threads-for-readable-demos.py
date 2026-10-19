import threading

def show_me():
    print(f"I am {threading.current_thread().name}")

t1 = threading.Thread(target=show_me, name="Worker-A")
t2 = threading.Thread(target=show_me, name="Worker-B")
t1.start(); t1.join()
t2.start(); t2.join()
