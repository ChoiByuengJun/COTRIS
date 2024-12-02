from game.entity.game import Game
from game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __init__(self):
        self.__game = None

    def create(self):
        playerCount = 2  # 두 명의 플레이어로 고정
        self.__game = Game(playerCount)

    def setPlayerIndexListToMap(self, playerIndexList, diceIdList):
        self.__game.setPlayerIndexListToMap(playerIndexList, diceIdList)

    def updatePlayerDiceGameMap(self, playerIndexList, diceIdList):
        self.__game.updatePlayerIndexListToMap(playerIndexList, diceIdList)

    def getGame(self):
        return self.__game

    def getGamePlayerCount(self):
        return self.__game.getPlayerCount()
