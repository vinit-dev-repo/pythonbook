# The "before" — print-debugging
def process_order(order_id, total):
    print(f"processing order {order_id}")
    if total < 0:
        print(f"ERROR: bad total {total} for order {order_id}")
    print("done")

# The "after" — a proper log line
import logging
logger = logging.getLogger(__name__)

def process_order_v2(order_id, total):
    logger.info("processing order %s", order_id)
    if total < 0:
        logger.error("bad total %s for order %s", total, order_id)
    logger.info("done")
