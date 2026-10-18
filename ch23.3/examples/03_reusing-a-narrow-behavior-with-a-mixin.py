class NameTagMixin:
    def name_tag(self):
        return f"[{self.name}]"

class Worker:
    def __init__(self, name):
        self.name = name

    def work(self):
        return "working"

class TaggedWorker(NameTagMixin, Worker):
    pass

worker = TaggedWorker("Ana")
print(worker.name_tag())
print(worker.work())
print([kind.__name__ for kind in TaggedWorker.__mro__])
