from abc import ABC, abstractmethod

class OrderService(ABC):

    @abstractmethod
    def orderFruit(self, buyerId, fruitId):
        pass