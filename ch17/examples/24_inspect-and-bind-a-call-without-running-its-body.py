import inspect

body_calls = []

def schedule(job, /, retries=2, *tags, urgent=False, **metadata):
    body_calls.append(job)
    return job, retries, tags, urgent, metadata

sig = inspect.signature(schedule)
for name, parameter in sig.parameters.items():
    has_default = parameter.default is not inspect.Parameter.empty
    print(name, parameter.kind.name, has_default)

bound = sig.bind("backup", urgent=True, owner="ops")
print(bound.arguments)
bound.apply_defaults()
print(bound.arguments)
print(body_calls)
print(schedule(*bound.args, **bound.kwargs))
print(body_calls)
