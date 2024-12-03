from django.db import models

class Game(models.Model):
    playerCount = models.IntegerField(default=2)
    playerDiceGameMap = models.JSONField(default=dict)  # JSON 형태로 주사위-플레이어 매핑 저장

    def getPlayerCount(self):
        return self.playerCount

    def getPlayerDiceGameMap(self):
        return self.playerDiceGameMap

    def setPlayerIndexListToMap(self, playerIndexList, diceIdList):
        self.playerDiceGameMap = {str(index): [diceId] for index, diceId in zip(playerIndexList, diceIdList)}
        self.save()

    def updatePlayerIndexListToMap(self, playerIndexList, diceIdList):
        for index, diceId in zip(playerIndexList, diceIdList):
            if str(index) in self.playerDiceGameMap:
                self.playerDiceGameMap[str(index)].append(diceId)
            else:
                self.playerDiceGameMap[str(index)] = [diceId]
        self.save()

    class Meta:
        db_table = "game"

