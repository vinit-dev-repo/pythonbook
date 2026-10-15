# compare_benchmarks.py
import json
from pathlib import Path
import subprocess
import sys

def compare(executables):
    worker = Path(__file__).with_name("benchmark_cases.py")
    for executable in executables:
        completed = subprocess.run(
            [executable, str(worker)], check=True, capture_output=True,
            text=True, timeout=30,
        )
        report = json.loads(completed.stdout)
        print(report["implementation"], report["version"], report["executable"])
        for result in report["results"]:
            print(result["case"], result["totals_seconds"],
                  result["best_seconds_per_call"])

if __name__ == "__main__":
    compare(sys.argv[1:] or [sys.executable])
