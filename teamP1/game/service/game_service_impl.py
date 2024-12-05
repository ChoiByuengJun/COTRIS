from game.service.game_service import GameService
from game.repository.game_repository_impl import GameRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl
from dice.repository.dice_repository_impl import DiceRepositoryImpl


class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
            cls.__instance.__playerRepository = PlayerRepositoryImpl.getInstance()
            cls.__instance.__diceRepository = DiceRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def startDiceGame(self):
        self.__gameRepository.create()
        print("게임을 시작합니다. 두 명의 플레이어가 참가합니다.")

    def rollingDice(self):

        playerIndexList = []
        diceIdList = []
        gamePlayerCount = self.__gameRepository.getGamePlayerCount() # 2명

        for playerIndex in range(gamePlayerCount):
            diceId = self.__diceRepository.rollDice()
            diceIdList.append(diceId)
            playerIndexList.append(playerIndex + 1)

        self.__gameRepository.updatePlayerDiceGameMap(playerIndexList, diceIdList)

    def printCurrentStatus(self):
        game = self.__gameRepository.getGame()
        playerDiceGameMap = game.getPlayerDiceGameMap()
        for playerId, diceIdList in playerDiceGameMap.items():
            diceNumbers = [self.__diceRepository.findById(diceId).getDiceNumber() for diceId in diceIdList]
            print(f"플레이어 {playerId}: {diceNumbers}")

    def checkWinner(self):
        game = self.__gameRepository.getGame()
        playerDiceGameMap = game.getPlayerDiceGameMap()

        scores = {}
        for playerId, diceIdList in playerDiceGameMap.items():
            scores[playerId] = sum(self.__diceRepository.findById(diceId).getDiceNumber() for diceId in diceIdList)

        maxScore = max(scores.values())
        winners = [playerId for playerId, score in scores.items() if score == maxScore]

        if len(winners) > 1:
            print("무승부입니다!")
        else:
            print(f"승자는 플레이어 {winners[0]}입니다!")

