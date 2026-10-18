# import_practice_package/myapp/utils/__init__.py
print("utils initializer")
from .library import label_pair
__all__ = ["label_pair"]
