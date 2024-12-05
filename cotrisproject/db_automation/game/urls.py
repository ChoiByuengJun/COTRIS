from django.urls import path, include
from rest_framework.routers import DefaultRouter


from game.controller.game_controller import GameController

# router = DefaultRouter()
# router.register(r"game", GameController, basename='game')
#
# urlpatterns = [
#     path('', include(router.urls)),
#     path('start/', GameController.as_view, ({'get': 'startGame' }),
#          name='게임 시작하기'),
#     path('<int:game_id>/roll/', GameController.as_view, ({'get': 'rollDice' }),
#          name='주사위 굴리기'),
#     path('<int:game_id>/status/', GameController.as_view, ({'get':'printStatus' }),
#          name='상태 표시하기'),
#     path('<int:game_id>/winner/', GameController.as_view, ({'get':'checkWinner' }),
#          name='승부 확인하기'),
# ]

from django.urls import path
from game.controller.game_controller import GameController

game_list = GameController.as_view({
    'get': 'startGame'
})

game_roll = GameController.as_view({
    'get': 'rollDice'
})

game_status = GameController.as_view({
    'get': 'printStatus'
})

game_winner = GameController.as_view({
    'get': 'checkWinner'
})

urlpatterns = [
    path('start/', game_list, name='게임 시작하기'),
    path('<int:gameId>/roll/', game_roll, name='주사위 굴리기'),
    path('<int:gameId>/status/', game_status, name='상태 표시하기'),
    path('<int:gameId>/winner/', game_winner, name='승부 확인하기'),
]
