# 3
import logging
import sys

logger = logging.getLogger("shop")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(levelname)s - %(name)s - %(message)s"))
logger.addHandler(handler)
logger.debug("hidden")
logger.info("started")
