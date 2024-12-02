class Game:
    def __init__(self, playerCount):
        self.__playerCount = playerCount
        self.__playerDiceGameMap = {}

    def getPlayerCount(self):
        return self.__playerCount

    def getPlayerDiceGameMap(self):
        return self.__playerDiceGameMap

    def setPlayerIndexListToMap(self, playerIndexList, diceIdList):
        self.__playerDiceGameMap = {index: [diceId] for index, diceId in zip(playerIndexList, diceIdList)}

    def updatePlayerIndexListToMap(self, playerIndexList, diceIdList):
        for index, diceId in zip(playerIndexList, diceIdList):
            if index in self.__playerDiceGameMap:
                self.__playerDiceGameMap[index].append(diceId)
            else:
                self.__playerDiceGameMap[index] = [diceId]
