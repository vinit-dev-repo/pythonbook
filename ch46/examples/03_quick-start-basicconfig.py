import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

logging.debug("starting up")
logging.info("loaded config")
logging.warning("config file was missing a value, used a default")
