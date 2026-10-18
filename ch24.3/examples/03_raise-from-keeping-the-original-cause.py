class AppError(Exception):
    pass

def load_config_quiet(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        raise AppError(f"Could not load config from {path}") from None

load_config_quiet("missing.txt")
