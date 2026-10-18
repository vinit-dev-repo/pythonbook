from enum import Enum, unique

class LabelledCode(Enum):
    def __new__(cls, code, label):
        member = object.__new__(cls)
        member._value_ = code
        member.label = label
        return member

@unique
class TaskCode(LabelledCode):
    DONE = (10, 'job done')
    FAILED = (20, 'job failed')

@unique
class SyncCode(LabelledCode):
    DONE = (10, 'sync done')

print(TaskCode.DONE.value, TaskCode.DONE.label)
print(SyncCode.DONE.value, SyncCode.DONE.label)
print(TaskCode.DONE == SyncCode.DONE)
print(TaskCode(10) is TaskCode.DONE)
