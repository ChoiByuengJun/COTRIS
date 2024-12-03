from game.entity.game import Game
from dice.entity.dice import Dice
from django.db import transaction


class GameService:
    @staticmethod
    @transaction.atomic
    def start_dice_game():
        game = Game.objects.create(player_count=2)
        print("게임이 시작되었습니다.")
        return game

    @staticmethod
    def rolling_dice(game_id):
        game = Game.objects.get(id=game_id)
        player_index_list = list(range(1, game.get_player_count() + 1))
        dice_id_list = []

        for player_index in player_index_list:
            dice = Dice.objects.create()  # 주사위를 굴려 저장
            dice_id_list.append(dice.id)

        game.update_player_index_list_to_map(player_index_list, dice_id_list)

    @staticmethod
    def print_current_status(game_id):
        game = Game.objects.get(id=game_id)
        player_dice_game_map = game.get_player_dice_game_map()

        for player_id, dice_id_list in player_dice_game_map.items():
            dice_numbers = [Dice.objects.get(id=dice_id).get_dice_number() for dice_id in dice_id_list]
            print(f"플레이어 {player_id}: {dice_numbers}")

    @staticmethod
    def check_winner(game_id):
        game = Game.objects.get(id=game_id)
        player_dice_game_map = game.get_player_dice_game_map()

        scores = {}
        for player_id, dice_id_list in player_dice_game_map.items():
            scores[player_id] = sum(Dice.objects.get(id=dice_id).get_dice_number() for dice_id in dice_id_list)

        max_score = max(scores.values())
        winners = [player_id for player_id, score in scores.items() if score == max_score]

        if len(winners) > 1:
            print("무승부입니다!")
        else:
            print(f"승자는 플레이어 {winners[0]}입니다!")
