class AppError(Exception):
    """Base class for expected application failures."""
    pass

class NotFoundError(AppError):
    pass

class ValidationError(AppError):
    pass
