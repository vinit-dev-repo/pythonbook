# class_counts.py
class Job:
    total = 0
    created = 0

    def __init__(self, label):
        if not isinstance(label, str):
            raise TypeError("label must be a string")
        self.label = label
        Job.total += 1
        type(self).record_creation()

    @classmethod
    def record_creation(cls):
        cls.created += 1

    @classmethod
    def count(cls):
        return cls.created

    @staticmethod
    def total_count():
        return Job.total

class LocalJob(Job):
    created = 0

class RemoteJob(Job):
    created = 0

base = Job("base")
first = LocalJob("one")
second = LocalJob("two")
remote = RemoteJob("remote")
print(Job.total_count(), first.total_count())
print(Job.count(), LocalJob.count(), remote.count())

class UnresetJob(Job):
    pass

print("before own count:", UnresetJob.count())
UnresetJob("inherits the initial value")
print("after own count:", UnresetJob.count(), Job.count())
