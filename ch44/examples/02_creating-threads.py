import threading
import time

def make_tea(minutes):
    print(f"Started brewing for {minutes}s")
    time.sleep(minutes)
    print("Tea is ready!")

t = threading.Thread(target=make_tea, args=(2,))
t.start()      # the worker starts working NOW, in the background
print("Meanwhile, I can do something else")
t.join()       # wait here until the worker is done
print("Both things are finished")
