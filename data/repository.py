from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, order):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

class InMemoryOrderRepository(Repository):
    pass