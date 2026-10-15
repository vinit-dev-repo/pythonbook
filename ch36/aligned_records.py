# aligned_records.py
from collections import namedtuple
from contextlib import ExitStack, contextmanager
from dataclasses import dataclass
from itertools import chain, compress, groupby

from managed_csv_records import prepare_reader, pack_row


@dataclass(frozen=True)
class FileSpec:
    path: object
    converters: dict


def typed_rows(reader, row_type, converters):
    if set(row_type._fields) != set(converters):
        raise ValueError("file header does not match its schema")
    while True:
        try:
            raw = pack_row(reader, row_type)
        except StopIteration:
            return
        values = [converters[name](value)
                  for name, value in zip(raw._fields, raw, strict=True)]
        yield row_type(*values)


@contextmanager
def aligned_records(specs, *, key="site_id", fields=None):
    specs = tuple(specs)
    if not specs:
        raise ValueError("at least one file is required")
    with ExitStack() as resources:
        streams, layouts = [], []
        for spec in specs:
            source = resources.enter_context(
                open(spec.path, encoding="utf-8", newline=""))
            reader, row_type = prepare_reader(source, delimiter=",")
            if key not in row_type._fields:
                raise ValueError("every file needs the join key")
            if set(row_type._fields) != set(spec.converters):
                raise ValueError("file header does not match its schema")
            stream = typed_rows(reader, row_type, spec.converters)
            resources.callback(stream.close)
            streams.append(stream)
            layouts.append(row_type._fields)

        all_names = tuple(chain.from_iterable(layouts))
        # Keep the key from file0 only; validate all copies before projecting.
        mask = tuple(i == 0 or name != key
                     for i, layout in enumerate(layouts) for name in layout)
        full_names = tuple(compress(all_names, mask))
        if len(set(full_names)) != len(full_names):
            raise ValueError("non-key field names must be unique across files")
        wanted = full_names if fields is None else tuple(fields)
        if len(set(wanted)) != len(wanted) or not set(wanted) <= set(full_names):
            raise ValueError("projection needs distinct known field names")
        positions = tuple(full_names.index(name) for name in wanted)
        Result = namedtuple("Joined", wanted)

        def joined():
            previous = None
            for records in zip(*streams, strict=True):
                keys = tuple(getattr(record, key) for record in records)
                if any(type(value) is not str or not value for value in keys):
                    raise ValueError("join keys must be nonempty strings")
                if len(set(keys)) != 1:
                    raise ValueError("rows refer to different keys")
                if previous is not None and keys[0] <= previous:
                    raise ValueError("join keys must be unique and increasing")
                previous = keys[0]
                values = tuple(compress(chain.from_iterable(records), mask))
                yield Result(*(values[position] for position in positions))

        rows = joined()
        resources.callback(rows.close)
        yield rows


def ranked_groups(records, *, accept, key):
    ordered = sorted(filter(accept, records), key=key)
    totals = [(name, sum(1 for _ in group))
              for name, group in groupby(ordered, key)]
    return sorted(totals, key=lambda item: (-item[1], item[0]))


def tied_leaders(ranking):
    if not ranking:
        return []
    best = ranking[0][1]
    return [item for item in ranking if item[1] == best]
