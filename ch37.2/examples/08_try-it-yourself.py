import functools
import gc

# 1
a = int("5000")
b = int("5000")
print(a == b)
print("same object in this run:", a is b)

# 2
_cache = {}
for number in range(1000):
    _cache[number] = number * 2
gc.collect()
print("plain dict after collect:", len(_cache))

@functools.lru_cache(maxsize=10)
def double(number):
    return number * 2

for number in range(1000):
    double(number)
print("bounded cache:", double.cache_info().currsize)

listeners = []
class Screen:
    def handle(self):
        pass

screen = Screen()
listeners.append(screen.handle)
gc.collect()
print("listener still held:", len(listeners))
listeners.remove(screen.handle)
print("after unregister:", len(listeners))

# 3
import tracemalloc

tracemalloc.start()
base = tracemalloc.get_traced_memory()[0]
kept = [str(i) for i in range(100_000)]
grown = tracemalloc.get_traced_memory()[0]
del kept
freed = tracemalloc.get_traced_memory()[0]
tracemalloc.stop()
print("grew by more than 1 MB:", grown - base > 1_000_000)
print("fell after the owner was released:", freed < grown)
