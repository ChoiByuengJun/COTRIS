from django.db import models


class Dice(models.Model):
    # 앞서 우리가 고유한 유일 숫자값 만들 것
    id = models.AutoField(primary_key=True)
    # 주사위 눈금은 숫자
    number = models.IntegerField()

    def __str__(self):
        return f"주사위 id: {self.id}, 눈금: {self.number}"

    def getId(self):
        return self.id

    def getNumber(self):
        return self.number

    class Meta:
        db_table = "dice"
