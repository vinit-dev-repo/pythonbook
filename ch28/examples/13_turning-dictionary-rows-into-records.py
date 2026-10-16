from collections import namedtuple

row = {"first-name": "Ada"}
try:
    namedtuple("Record", row.keys())
except ValueError as error:
    print("invalid field:", type(error).__name__)

Renamed = namedtuple("Renamed", row.keys(), rename=True)
try:
    Renamed(**row)
except TypeError as error:
    print("original keyword:", type(error).__name__)
