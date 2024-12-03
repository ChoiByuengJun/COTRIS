from django.http import JsonResponse
from game.services import GameService


def start_game(request):
    game = GameService.start_dice_game()
    return JsonResponse({"message": "게임이 시작되었습니다.", "game_id": game.id})


def roll_dice(request, game_id):
    GameService.rolling_dice(game_id)
    return JsonResponse({"message": "주사위를 굴렸습니다.", "game_id": game_id})


def print_status(request, game_id):
    GameService.print_current_status(game_id)
    return JsonResponse({"message": "게임 상태를 출력했습니다.", "game_id": game_id})


def check_winner(request, game_id):
    GameService.check_winner(game_id)
    return JsonResponse({"message": "승자를 확인했습니다.", "game_id": game_id})
