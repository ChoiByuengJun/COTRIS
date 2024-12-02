from abc import ABC, abstractmethod


class DiceRepository(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findAll(self):
        pass
