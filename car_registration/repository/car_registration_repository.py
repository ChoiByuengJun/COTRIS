from abc import ABC, abstractmethod


class CarRegistrationRepository(ABC):

    @abstractmethod
    def createMany(self, carRegistrationData):
        pass

    @abstractmethod
    def findAll(self):
        pass
