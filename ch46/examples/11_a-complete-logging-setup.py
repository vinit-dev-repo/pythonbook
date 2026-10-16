import logging.config

config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "%(levelname)s %(name)s: %(message)s"},
        "detailed": {"format": "%(asctime)s %(levelname)s %(name)s [%(lineno)d]: %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
        },
        "all_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "detailed",
            "filename": "app.log",
            "maxBytes": 2_000_000,
            "backupCount": 5,
        },
        "errors_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "detailed",
            "filename": "errors.log",
            "maxBytes": 2_000_000,
            "backupCount": 5,
        },
    },
    "loggers": {
        "app": {"level": "DEBUG", "handlers": ["console", "all_file", "errors_file"], "propagate": False},
        "app.db": {"level": "DEBUG", "handlers": ["console", "all_file", "errors_file"], "propagate": False},
        "app.api": {"level": "DEBUG", "handlers": ["console", "all_file", "errors_file"], "propagate": False},
    },
}

logging.config.dictConfig(config)

app_logger = logging.getLogger("app")
db_logger = logging.getLogger("app.db")
api_logger = logging.getLogger("app.api")

app_logger.info("application starting")
db_logger.debug("opened connection pool of size 5")
api_logger.warning("rate limit at %d%% of quota", 80)   # %% only becomes a literal % once a real %-style arg follows

try:
    1 / 0
except ZeroDivisionError:
    db_logger.exception("query failed unexpectedly")
