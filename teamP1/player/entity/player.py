class Player:
    __counter = 1

    def __init__(self, playerName):
        self.__playerName = playerName
        self.__id = Player.__counter
        Player.__counter += 1
        self.__diceIdList = []

    def addDiceId(self, diceId):
        self.__diceIdList.append(diceId)

    def __str__(self):
        return f"{self.__playerName} (주사위: {self.__diceIdList})"
