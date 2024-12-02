from game.service.game_service_impl import GameServiceImpl

gameService = GameServiceImpl.getInstance()
gameService.startDiceGame()
gameService.rollingDice()
gameService.printCurrentStatus()
gameService.rollingDice()
gameService.printCurrentStatus()
gameService.checkWinner()
