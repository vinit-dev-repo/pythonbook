# timed_methods.py
from method_tools import method_metaclass, decorate_methods, make_bucket
from timing_tools import call_timings

for mode in ("meta", "decorator"):
    samples = iter([0.0, 0.5, 1.0, 1.25, 2.0, 2.75])
    timing = call_timings(label=mode, clock=samples.__next__)
    if mode == "meta":
        Bucket = make_bucket(meta=method_metaclass(timing))
    else:
        Bucket = make_bucket(decorate=decorate_methods(timing))
    item = Bucket()
    print(mode, item.add(2), item.report())
    print(Bucket.__init__.stats["total"], Bucket.add.stats["total"], Bucket.report.stats["total"])
