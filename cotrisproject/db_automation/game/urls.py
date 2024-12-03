from django.urls import path
from game.controller.game_controller import start_game, roll_dice, print_status, check_winner

urlpatterns = [
    path('start/', start_game, name='start_game'),
    path('<int:game_id>/roll/', roll_dice, name='roll_dice'),
    path('<int:game_id>/status/', print_status, name='print_status'),
    path('<int:game_id>/winner/', check_winner, name='check_winner'),
]
