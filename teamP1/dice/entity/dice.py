class Dice:
    __counter = 1

    def __init__(self, diceNumber):
        self.__diceNumber = diceNumber
        self.__id = Dice.__counter
        Dice.__counter += 1

    def __str__(self):
        return f"dice number: {self.__number}"

    def getId(self):
        return self.__id

    def getDiceNumber(self):
        return self.__number
