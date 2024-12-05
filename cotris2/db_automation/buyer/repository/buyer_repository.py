from abc import ABC, abstractmethod


class BuyerRepository(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def findById(self, id):
        pass