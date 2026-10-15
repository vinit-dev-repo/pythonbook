# base_demo.py
from fields import BaseValidator


class Storage:
    value = BaseValidator()


if __name__ == "__main__":
    item = Storage()
    token = object()
    item.value = token
    print(item.value is token)
    item.value = None
    print(item.value is None)
