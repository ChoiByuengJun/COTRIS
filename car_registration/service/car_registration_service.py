from abc import ABC, abstractmethod


class CarRegistrationService(ABC):

    @abstractmethod
    def createCarRegistration(self):
        pass

    @abstractmethod
    def carRegistrationList(self):
        pass
