# 3
import io
import logging

buffer = io.StringIO()
handler = logging.StreamHandler(buffer)
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger = logging.getLogger("lookup")
logger.addHandler(handler)

try:
    {"a": 1}["b"]
except KeyError:
    logger.exception("lookup failed")

lines = buffer.getvalue().splitlines()
print(lines[0])
print(lines[-1])
