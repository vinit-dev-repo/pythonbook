# 1
import csv
with open("people.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Asha", 30])
    writer.writerow(["Ravi", 25])

with open("people.csv", "r", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["age"])

# 2
import random
random.seed(7)
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
# run it again -- same three numbers both times

# 3
import timeit
as_list = [i * 2 for i in range(100)]
as_map = list(map(lambda i: i * 2, range(100)))
assert as_list == as_map
print(timeit.repeat("[i * 2 for i in range(100)]", number=10_000, repeat=3))
print(timeit.repeat("list(map(lambda i: i * 2, range(100)))", number=10_000, repeat=3))
