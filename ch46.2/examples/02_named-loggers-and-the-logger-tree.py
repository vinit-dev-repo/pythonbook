import logging

logging.basicConfig(level=logging.INFO, format="%(name)s: %(message)s")

orders_logger = logging.getLogger("myapp.orders")
orders_logger.info("order 42 placed")
