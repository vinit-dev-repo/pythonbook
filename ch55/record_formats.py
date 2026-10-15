# record_formats.py
import json

formats = {}

def register_format(label):
    def register(function):
        if label in formats:
            raise ValueError("format label already registered")
        formats[label] = function
        return function
    return register

@register_format("compact")
def compact(record):
    return json.dumps(record, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False)

@register_format("indented")
def indented(record):
    return json.dumps(record, sort_keys=True, ensure_ascii=False,
                      indent=2, allow_nan=False)

def smallest(record, candidates=None):
    choices = tuple(formats.items() if candidates is None else candidates)
    if not choices:
        raise ValueError("at least one format is required")
    expected = json.dumps(record, sort_keys=True, allow_nan=False)
    results = []
    for label, format_record in choices:
        text = format_record(record)
        restored = json.loads(text)
        if json.dumps(restored, sort_keys=True, allow_nan=False) != expected:
            raise ValueError("format changed the record")
        results.append((label, text))
    return min(results, key=lambda item: len(item[1].encode("utf-8")))
