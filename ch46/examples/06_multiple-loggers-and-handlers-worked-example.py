import logging

logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)          # let everything through to the handlers below

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

file_handler = logging.FileHandler("myapp.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("connecting to database")
logger.info("server started on port 8000")
logger.warning("cache is nearly full")
