import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.exception("division failed")

divide(10, 0)
