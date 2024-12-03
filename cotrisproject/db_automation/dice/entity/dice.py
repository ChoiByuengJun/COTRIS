from django.db import models


class Dice(models.Model):
    id = models.AutoField(primary_key=True)
    dice_number = models.IntegerField()

    def __str__(self):
        return f"Dice id: {self.id}, 눈금: {self.dice_number}"

    def get_id(self):
        return self.id

    def get_dice_number(self):
        return self.dice_number

    class Meta:
        db_table = "dice"
