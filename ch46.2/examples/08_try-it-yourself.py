# 2
import io
import logging
import sys

logger = logging.getLogger("disk")
logger.setLevel(logging.DEBUG)
layout = logging.Formatter("%(levelname)s: %(message)s")

console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.WARNING)
console.setFormatter(layout)

buffer = io.StringIO()
kept = logging.StreamHandler(buffer)
kept.setLevel(logging.DEBUG)
kept.setFormatter(layout)

logger.addHandler(console)
logger.addHandler(kept)
logger.debug("checking")
logger.warning("low disk")
print("lines kept in the buffer:", len(buffer.getvalue().splitlines()))
