# 1
import logging
import sys

parent = logging.getLogger("myapp")
parent.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(name)s: %(message)s"))
parent.addHandler(handler)

child = logging.getLogger("myapp.orders")
child.info("order 42 placed")
child.propagate = False
child.info("this one stops at the child")
