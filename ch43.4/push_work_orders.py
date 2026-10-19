# push_work_orders.py
import csv
from contextlib import ExitStack, contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory

HEADER = ["task", "tags", "minutes"]

def send_to_writer(writer):
    while True:
        row = yield
        writer.writerow(row)

def keep_if(predicate, target):
    while True:
        row = yield
        if predicate(row):
            target.send(row)

@contextmanager
def csv_pipeline(target_path, predicates):
    predicates = tuple(predicates)
    with ExitStack() as resources:
        stream = resources.enter_context(
            target_path.open("w", encoding="utf-8", newline="")
        )
        writer = csv.writer(stream)
        writer.writerow(HEADER)

        def own(stage):
            resources.callback(stage.close)
            next(stage)
            return stage

        head = own(send_to_writer(writer))
        # Building backward makes the first predicate receive each row first.
        for predicate in reversed(predicates):
            head = own(keep_if(predicate, head))
        yield head

def export_orders(source_path, target_path, required_tags):
    if source_path.resolve() == target_path.resolve():
        raise ValueError("use a separate output file")
    required_tags = tuple(required_tags)
    if any(type(tag) is not str or not tag or ";" in tag for tag in required_tags):
        raise ValueError("tags must be nonempty strings without semicolons")
    predicates = [lambda row, wanted=tag: wanted in row[1].split(";")
                  for tag in required_tags]
    with source_path.open(encoding="utf-8", newline="") as stream:
        rows = csv.reader(stream, strict=True)
        if next(rows, None) != HEADER:
            raise ValueError("unexpected input header")
        with csv_pipeline(target_path, predicates) as head:
            for row in rows:
                if len(row) != len(HEADER):
                    raise ValueError("expected three fields")
                head.send(row)

def main():
    with TemporaryDirectory() as directory:
        root = Path(directory)
        source, target = root / "orders.csv", root / "selected.csv"
        sample = [
            ["Inspect lamps, hall", "inside;urgent", "35"],
            ["Paint rail", "outside;urgent", "50"],
            ["Read meter", "inside", "5"],
            ["Check panel", "inside;urgent", "10"],
        ]
        with source.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream)
            writer.writerow(HEADER)
            writer.writerows(sample)
        export_orders(source, target, ["inside", "urgent"])
        with target.open(encoding="utf-8", newline="") as stream:
            for row in csv.reader(stream):
                print(" | ".join(row))

if __name__ == "__main__":
    main()
