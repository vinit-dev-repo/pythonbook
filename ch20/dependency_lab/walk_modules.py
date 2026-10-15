# dependency_lab/walk_modules.py
from types import ModuleType

def inspect_modules(start):
    pending = [start]
    seen = set()
    visited = []
    trace = []
    while pending:
        current = pending.pop()
        if current in seen:
            action = "skip"
        else:
            action = "visit"
            seen.add(current)
            visited.append(current)
            children = [
                value
                for name, value in sorted(current.__dict__.items())
                if isinstance(value, ModuleType)
            ]
            pending.extend(children)
        trace.append((
            current.__name__, action,
            [item.__name__ for item in pending],
            sorted(item.__name__ for item in seen),
        ))
    return visited, trace
