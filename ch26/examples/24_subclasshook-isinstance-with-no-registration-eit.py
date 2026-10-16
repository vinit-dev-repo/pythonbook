import _collections_abc

with open(_collections_abc.__file__, encoding="utf-8") as f:
    lines = f.readlines()

start = next(i for i, line in enumerate(lines) if line.startswith("class Sized"))
end = next(i for i, line in enumerate(lines[start + 1:], start + 1)
           if line.startswith("class "))

print("".join(lines[start:end]).rstrip())
print()

start2 = next(i for i, line in enumerate(lines) if line.startswith("def _check_methods"))
print("".join(lines[start2:start2 + 11]).rstrip())
