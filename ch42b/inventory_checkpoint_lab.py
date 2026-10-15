# inventory_checkpoint_lab.py
from collections import Counter, defaultdict
from dataclasses import dataclass

def by_value(mapping):
    return dict(sorted(mapping.items(), key=lambda pair: pair[1]))

def paired(left, right):
    return {key: (left[key], right[key]) for key in sorted(left.keys() & right.keys())}

def ranked(mapping):
    return dict(sorted(mapping.items(), key=lambda pair: pair[1], reverse=True))

def plain_totals(*stations):
    result = {}
    for station in stations:
        for category, count in station.items():
            result[category] = result.get(category, 0) + count
    return ranked(result)

def factory_totals(*stations):
    result = defaultdict(int)
    for station in stations:
        for category, count in station.items():
            result[category] += count
    return ranked(result)

def counter_totals(*stations):
    result = Counter()
    for station in stations:
        result.update(station)
    return dict(result.most_common())

def partial_reports(first, second, third):
    any_station = first.keys() | second.keys() | third.keys()
    every_station = first.keys() & second.keys() & third.keys()
    return {key: tuple(station.get(key, 0) for station in (first, second, third))
            for key in sorted(any_station - every_station)}

@dataclass
class Specimen:
    category: str

def category_counts(specimens, categories):
    counts = Counter(dict.fromkeys(categories, 0))
    for specimen in specimens:
        if specimen.category not in counts:
            raise ValueError("unknown specimen category")
        counts.update([specimen.category])
    return dict(counts)

stations = ({"fern": 0, "moss": 2}, {"fern": 3, "lichen": 1}, {"fern": 0, "moss": 1})
print(by_value({"east": 5, "west": 2, "island": 2}))
print(paired(stations[0], stations[1]))
result = plain_totals(*stations)
print(result)
print("same ordered items:", list(result.items()) == list(factory_totals(*stations).items()) == list(counter_totals(*stations).items()))
print(partial_reports(*stations))
print(category_counts([Specimen("moss"), Specimen("moss")], ["fern", "moss", "lichen"]))
