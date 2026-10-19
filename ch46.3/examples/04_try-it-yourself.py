# 1
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("d")
logging.info("i")
logging.warning("w")
logging.error("e")
logging.critical("c")

# 2
logger = logging.getLogger("shop.checkout")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)
logger.propagate = False  # keep records from also reaching exercise 1's DEBUG root handler
logger.debug("this will not print on the console handler")
logger.info("this will")

# 3
from logging.handlers import RotatingFileHandler
file_handler = RotatingFileHandler("small.log", maxBytes=500, backupCount=2)
file_handler.setLevel(logging.DEBUG)
logger2 = logging.getLogger("rotdemo")
logger2.setLevel(logging.DEBUG)
logger2.addHandler(file_handler)
for i in range(50):
    logger2.debug(f"log line number {i}, padded to be a bit longer")

# 4
try:
    d = {"a": 1}
    print(d["b"])
except KeyError:
    logging.getLogger(__name__).exception("missing key")

# 5
# Stop at this logger: exercise 1 already configured a root handler.
import logging.config
cfg = {
    "version": 1,
    "handlers": {
        "console": {"class": "logging.StreamHandler", "level": "INFO"},
        "file": {"class": "logging.FileHandler", "level": "ERROR", "filename": "errors_only.log"},
    },
    "loggers": {
        "demo": {"level": "DEBUG", "handlers": ["console", "file"], "propagate": False},
    },
}
logging.config.dictConfig(cfg)
d_logger = logging.getLogger("demo")
d_logger.info("everything is fine")
d_logger.error("something broke")
