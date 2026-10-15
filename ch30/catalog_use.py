# catalog_use.py
from error_catalog import Catalog

for member in Catalog:
    for message in (None, "custom", ""):
        try:
            member.throw(message)
        except Exception as error:
            print(member.name, type(error).__name__, repr(str(error)))
try:
    Catalog.BAD_NAME.throw(42)
except TypeError as error:
    print(type(error).__name__ + ":", error)

catalog_rows = [
    {"code": item.code, "name": item.name,
     "type": item.exception_type.__name__, "message": item.default_message}
    for item in Catalog
]
print(catalog_rows)
