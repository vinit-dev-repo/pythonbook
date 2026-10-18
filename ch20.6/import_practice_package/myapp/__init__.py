# import_practice_package/myapp/__init__.py
print("myapp initializer")
from .utils import label_pair
__all__ = ["label_pair"]
