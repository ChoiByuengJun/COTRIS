import random

class DiceRoller:
    def __init__(self, name):
        self.name = name

    def roll_dice(self):
        return random.randint(1, 6)  # 1부터 6까지의 주사위 값

player1 = DiceRoller(name="Player 1")
player2 = DiceRoller(name="Player 2")

players = [player1, player2]

for player in players:
    roll_1 = player.roll_dice()
    roll_2 = player.roll_dice()

    print("display")
