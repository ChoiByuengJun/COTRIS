from abc import ABC, abstractmethod


class BuyerRepository(ABC):

    @abstractmethod
    def create(self):
        pass