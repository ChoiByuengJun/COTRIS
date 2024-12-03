from player.entity.player import Player
from player.repository.player_repository import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):
    __instance = None
    __players = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def createName(self):
        playerName = input("플레이어 이름을 입력하세요: ")
        player = Player(playerName)
        self.__players.append(player)

        return self.__players

    def findById(self, playerId):
        for player in self.__players:
            if player.getId() == playerId:
                return player
        return None
