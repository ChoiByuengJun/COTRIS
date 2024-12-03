class Game:
    def __init__(self, playerCount):
        self.__playerCount = playerCount
        self.__playerDiceGameMap = {}

    def getPlayerCount(self):
        return self.__playerCount

    def getPlayerDiceGameMap(self): #플레이어와 플레이어가 굴린 매핑 정보 반환
        return self.__playerDiceGameMap

    def setPlayerIndexListToMap(self, playerIndexList, diceIdList): #각 플레이어와 그들이 굴린 주사위를 매핑합니다.
        self.__playerDiceGameMap = {index: [diceId] for index, diceId in zip(playerIndexList, diceIdList)}

    def updatePlayerIndexListToMap(self, playerIndexList, diceIdList):
        for index, diceId in zip(playerIndexList, diceIdList):
            if index in self.__playerDiceGameMap:
                self.__playerDiceGameMap[index].append(diceId)
            else:
                self.__playerDiceGameMap[index] = [diceId]
