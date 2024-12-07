from abc import ABC, abstractmethod


class CarBusinessPricingService(ABC):

    @abstractmethod
    def createCarBusinessPricing(self):
        pass

    @abstractmethod
    def carBusinessPricingList(self):
        pass
