# 1
import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", stream=sys.stdout)
logging.debug("d")
logging.info("i")
logging.warning("w")
logging.error("e")
logging.critical("c")
