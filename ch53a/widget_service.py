# widget_service.py
from widget_errors import OutOfStock, Inventory, Pricing, Supplier, Checkout


def run_checkout(operation, observations):
    try:
        return operation()
    except OutOfStock:
        observations.append('OutOfStock')
        raise
    except Inventory:
        observations.append('Inventory')
        raise
    except Pricing:
        observations.append('Pricing')
        raise
    except Supplier:
        observations.append('Supplier')
        raise
    except Checkout:
        observations.append('Checkout')
        raise
