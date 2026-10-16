from logging.handlers import TimedRotatingFileHandler

handler = TimedRotatingFileHandler(
    "app.log",
    when="midnight",   # roll over at midnight every day
    interval=1,
    backupCount=14,    # keep at most 14 backup files
)
