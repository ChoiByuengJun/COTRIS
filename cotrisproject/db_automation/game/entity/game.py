from django.db import models

class Game(models.Model):
    player_count = models.IntegerField(default=2)
    player_dice_game_map = models.JSONField(default=dict)  # JSON 형태로 주사위-플레이어 매핑 저장

    def get_player_count(self):
        return self.player_count

    def get_player_dice_game_map(self):
        return self.player_dice_game_map

    def set_player_index_list_to_map(self, player_index_list, dice_id_list):
        self.player_dice_game_map = {str(index): [dice_id] for index, dice_id in zip(player_index_list, dice_id_list)}
        self.save()

    def update_player_index_list_to_map(self, player_index_list, dice_id_list):
        for index, dice_id in zip(player_index_list, dice_id_list):
            if str(index) in self.player_dice_game_map:
                self.player_dice_game_map[str(index)].append(dice_id)
            else:
                self.player_dice_game_map[str(index)] = [dice_id]
        self.save()
