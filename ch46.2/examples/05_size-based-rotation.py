import logging
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(
    "app.log",
    maxBytes=1_000_000,   # start a new file after ~1 MB
    backupCount=5,        # keep at most 5 old files
)
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))

logger = logging.getLogger("myapp")
logger.setLevel(logging.INFO)
logger.addHandler(handler)

logger.info("writing to a size-limited, rotating log file")
