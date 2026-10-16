def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as original:
        raise AppError(f"Could not load config from {path}") from original

load_config("missing.txt")
