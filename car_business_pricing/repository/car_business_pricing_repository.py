from abc import ABC, abstractmethod


class CarBusinessPricingRepository(ABC):

    @abstractmethod
    def createMany(self, carBusinessPricingDataList):
        pass
