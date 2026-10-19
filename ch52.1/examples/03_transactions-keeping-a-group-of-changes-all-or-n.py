try:
    connection.execute(...)
    connection.execute(...)
    connection.commit()
except Exception:
    connection.rollback()
    raise
