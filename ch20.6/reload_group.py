# reload_group.py
import importlib
import sys
from pathlib import Path
from tempfile import TemporaryDirectory


def dependency_order(dependencies):
    names = set(dependencies)
    if any(child not in names for children in dependencies.values()
           for child in children):
        raise ValueError("undeclared dependency")
    remaining = list(dependencies)
    finished = set()
    order = []
    while remaining:
        ready = next((name for name in remaining
                      if all(child in finished
                             for child in dependencies[name])), None)
        if ready is None:
            raise ValueError("dependency cycle")
        remaining.remove(ready)
        finished.add(ready)
        order.append(ready)
    return order


dependencies = {
    "lab_report": ("lab_left", "lab_right"),
    "lab_left": ("lab_rate",),
    "lab_right": ("lab_rate",),
    "lab_rate": (),
}
order = dependency_order(dependencies)
print("order:", order)
with TemporaryDirectory() as folder:
    root = Path(folder)
    sources = {
        "lab_rate": "RATE = 2\n",
        "lab_left": "from lab_rate import RATE\n",
        "lab_right": "from lab_rate import RATE\n",
        "lab_report": "import lab_left, lab_right\n"
                      "def values():\n"
                      "    return lab_left.RATE, lab_right.RATE\n",
    }
    for name, source in sources.items():
        (root / f"{name}.py").write_text(source, encoding="utf-8")
    sys.path.insert(0, folder)
    try:
        report = importlib.import_module("lab_report")
        modules = {name: sys.modules[name] for name in order}
        saved_rate = modules["lab_left"].RATE
        (root / "lab_rate.py").write_text("RATE = 300\n", encoding="utf-8")
        importlib.invalidate_caches()
        importlib.reload(modules["lab_rate"])
        print("child only:", report.values())
        for name in order:
            modules[name] = importlib.reload(modules[name])
        print("whole group:", report.values())
        print("outside binding:", saved_rate)

        (root / "lab_rate.py").write_text("RATE = 4000\n", encoding="utf-8")
        (root / "lab_left.py").write_text(
            "from lab_rate import RATE\nraise RuntimeError('broken client')\n",
            encoding="utf-8",
        )
        try:
            for name in order:
                modules[name] = importlib.reload(modules[name])
        except RuntimeError:
            print("failed group:", report.values())
    finally:
        sys.path.remove(folder)
        for name in dependencies:
            sys.modules.pop(name, None)
