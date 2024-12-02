from abc import ABC, abstractmethod


class DiceService(ABC):

    @abstractmethod
    def rollDice(self):
        pass

    @abstractmethod
    def findDice(self, requestDiceId):
        pass

    @abstractmethod
    def findEveryDice(self):
        pass
