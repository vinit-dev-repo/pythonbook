from tracer_lab import Tracer

traced_list = Tracer(list)(["a"])
traced_list.append("b")
print(traced_list.pop())
print(traced_list._target)
