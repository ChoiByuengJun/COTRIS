from abc import ABC, abstractmethod


class GameService(ABC):

    @abstractmethod
    def startDiceGame(self):
        pass

    @abstractmethod
    def rollingDice(self):
        pass

    @abstractmethod
    def printCurrentStatus(self):
        pass

    @abstractmethod
    def checkWinner(self):
        pass

