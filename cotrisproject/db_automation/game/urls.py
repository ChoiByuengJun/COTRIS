from django.urls import path, include
from rest_framework.routers import DefaultRouter


from game.controller.game_controller import GameController

router = DefaultRouter()
router.register(r"game", GameController, basename='game')

urlpatterns = [
    path('', include(router.urls)),
    path('start/', GameController.as_view, name='startGame'),
    path('<int:game_id>/roll/', GameController.as_view, name='rollDice'),
    path('<int:game_id>/status/', GameController.as_view, name='printStatus'),
    path('<int:game_id>/winner/', GameController.as_view, name='checkWinner'),
]
