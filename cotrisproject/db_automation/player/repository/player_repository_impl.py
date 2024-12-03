from django.shortcuts import get_object_or_404

from player.entity.player import Player


class PlayerRepositoryImpl:
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

    def createName(self):
        playerName = input("플레이어 이름을 입력하세요: ")
        player = Player.objects.create(name=playerName)
        return player

    def findById(self, playerId):
        player = get_object_or_404(Player, id=playerId)
        return player