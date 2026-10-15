# profile_report.py
import cProfile
from pathlib import Path
import pstats

from report import summarize_indexed, summarize_naive


def build_workload():
    categories = [f"category_{number}" for number in range(40)]
    rows = [
        {"category": categories[number % len(categories)], "quantity": 1}
        for number in range(20_000)
    ]
    return rows, categories


def helper_calls(stats):
    for function, values in stats.stats.items():
        if function[2] == "category_total":
            return values[1]
    return 0


def profile_summary(name, summary, rows, categories):
    profiler = cProfile.Profile()
    result = profiler.runcall(summary, rows, categories)
    profile_path = Path(f"{name}.prof")
    profiler.dump_stats(profile_path)

    with Path(f"{name}_stats.txt").open("w", encoding="utf-8") as stream:
        stats = pstats.Stats(profiler, stream=stream)
        stats.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE).print_stats("report")
        stats.sort_stats(pstats.SortKey.TIME).print_stats("report")

    stats = pstats.Stats(str(profile_path))
    return result, helper_calls(stats)


if __name__ == "__main__":
    rows, categories = build_workload()
    naive_result, naive_calls = profile_summary(
        "naive", summarize_naive, rows, categories
    )
    indexed_result, indexed_calls = profile_summary(
        "indexed", summarize_indexed, rows, categories
    )
    assert naive_result == indexed_result
    assert sum(naive_result.values()) == 20_000
    print(f"Naive helper calls: {naive_calls}")
    print(f"Indexed helper calls: {indexed_calls}")
