# catalog_metadata.py
from error_catalog import Catalog


if __name__ == '__main__':
    by_code = Catalog(100)
    by_name = Catalog['BAD_NAME']
    original = by_code.default_message
    try:
        by_code.default_message = 'temporary metadata'
        print(by_code is by_name, by_code.code, by_name.default_message)
        try:
            by_code.throw('custom')
        except ValueError as error:
            print(str(error))
        print('still:', by_name.default_message)
    finally:
        by_code.default_message = original
    print(Catalog.BAD_NAME.default_message)
