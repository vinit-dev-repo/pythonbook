from error_catalog import Catalog

errors = []
for message in ("custom", None):
    try:
        Catalog.BAD_NAME.throw(message)
    except ValueError as error:
        errors.append(error)
print("same exception:", errors[0] is errors[1])
print("messages:", [str(error) for error in errors])
print("default:", Catalog.BAD_NAME.default_message)
print("same member:", Catalog(100) is Catalog.BAD_NAME)
