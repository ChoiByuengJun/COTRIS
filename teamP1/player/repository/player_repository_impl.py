from player.entity.player import Player
from player.repository.player_repository import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):

    __instance = None
    __playerList = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def __inputPlayerName(self):
        inputPlayerName = input("플레이어 이름을 입력해주세요: ")
        return inputPlayerName

    def createName(self):
        playerName = self.__inputPlayerName()
        player = Player(playerName)

        self.__playerList.append(player)

    def acquirePlayerList(self):
        return self.__playerList

    def findById(self, id):
        for player in self.__playerList:
            if player.getId() == id:
                return player

        return None