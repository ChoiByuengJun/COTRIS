from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from game.service.game_service_impl import GameServiceImpl


class GameController(viewsets.ViewSet):
    gameService = GameServiceImpl.getInstance()

    def startGame(self, request):
        game = self.gameService.startDiceGame()
        return Response(game, status=status.HTTP_200_OK)


    def rollDice(self, request, gameId):
        self.gameService.rollingDice(gameId)
        return Response(
            model_to_dict(self.rollDice),
            status=status.HTTP_200_OK)

    def printStatus(self, request, gameId):
        self.gameService.printCurrentStatus(gameId)
        return

    def checkWinner(self, request, gameId):
        self.gameService.checkWinner(gameId)
        return