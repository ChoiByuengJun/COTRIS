class Player:
    __counter = 1

    def __init__(self, playerName):
        self.__playerName = playerName
        self.__id = Player.__counter
        Player.__counter += 1

    def __str__(self):
        return f"Player(name: {self.__playerName}, diceId: {self.__diceIdList})"

    def getId(self):
        return self.__id
