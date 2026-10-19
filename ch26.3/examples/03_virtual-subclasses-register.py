import abc


class Archive(abc.ABC):
    @abc.abstractmethod
    def save(self, item):
        pass


@Archive.register
class ArchivedGateway:
    def save(self, item):
        return item


print(ArchivedGateway.__name__)
print(isinstance(ArchivedGateway(), Archive))
