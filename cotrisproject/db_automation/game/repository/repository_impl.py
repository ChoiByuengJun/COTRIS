from game.models import Game
from repositories.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):
    @staticmethod
    def create():
        return Game.objects.create(player_count=2)

    @staticmethod
    def set_player_index_list_to_map(game, player_index_list, dice_id_list):
        game.set_player_index_list_to_map(player_index_list, dice_id_list)

    @staticmethod
    def update_player_dice_game_map(game, player_index_list, dice_id_list):
        game.update_player_index_list_to_map(player_index_list, dice_id_list)
