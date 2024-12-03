from abc import ABC, abstractmethod

class GameRepository(ABC):

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def set_player_index_list_to_map(self, player_index_list, dice_id_list):
        pass

    @abstractmethod
    def update_player_dice_game_map(self, player_index_list, dice_id_list):
        pass
