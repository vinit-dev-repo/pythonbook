import itertools

def noisy():
    for i in range(3):
        print(f"  read {i}")
        yield i

print("creating the product...")
pairs = itertools.product(noisy(), repeat=2)
print("created - and the input is already gone")
