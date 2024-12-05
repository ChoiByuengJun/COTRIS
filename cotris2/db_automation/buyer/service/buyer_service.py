from abc import ABC, abstractmethod


class BuyerService(ABC):

    @abstractmethod
    def createBuyer(self, id):
        pass
