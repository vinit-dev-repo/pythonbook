# compare_formats.py
import inspect
import record_formats

record = {"units": 2, "code": "K4"}
label, text = record_formats.smallest(record)
print(label)
print(text)
print(record_formats.formats["compact"] is record_formats.compact)
discovered = [name for name, function in
              inspect.getmembers(record_formats, inspect.isfunction)]
print(discovered)
