from abc import ABC, abstractmethod


class OrderRepository(ABC):

    @abstractmethod
    def order(self, fruit, buyer):
        pass