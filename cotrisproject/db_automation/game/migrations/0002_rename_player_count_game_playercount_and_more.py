# Generated by Django 5.1.3 on 2024-12-04 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="game",
            old_name="player_count",
            new_name="playerCount",
        ),
        migrations.RenameField(
            model_name="game",
            old_name="player_dice_game_map",
            new_name="playerDiceGameMap",
        ),
        migrations.AlterModelTable(
            name="game",
            table="game",
        ),
    ]