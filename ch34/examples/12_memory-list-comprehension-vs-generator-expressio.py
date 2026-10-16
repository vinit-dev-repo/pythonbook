import sys

big_list = [x for x in range(1_000_000)]
big_gen = (x for x in range(1_000_000))

print(sys.getsizeof(big_list))    # a real number of bytes -- grows with size
print(sys.getsizeof(big_gen))      # a small, FIXED number of bytes
