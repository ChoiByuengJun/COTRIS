from rest_framework import serializers

from dice.entity.dice import Dice


class DiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dice
        fields = ['id', 'number']
        # fields = ['number']
