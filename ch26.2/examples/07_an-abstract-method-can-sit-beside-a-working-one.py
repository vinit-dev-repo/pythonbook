import abc

class LabelledJob(abc.ABC):
    @abc.abstractmethod
    def label(self):
        return "job"

class EmailJob(LabelledJob):
    def label(self):
        return f"email-{super().label()}"

try:
    LabelledJob()
except TypeError as error:
    print(type(error).__name__)
print(EmailJob().label())
