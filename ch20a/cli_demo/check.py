# cli_demo/check.py
import labels
print(labels.make_label("hello", count=2))
labels.self_test()
try:
    labels.make_label("hello", count=0)
except ValueError as error:
    print(error)
