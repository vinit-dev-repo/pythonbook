# Inside a library module — correct habit
import logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())   # stay silent until the app configures logging
