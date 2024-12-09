from django.db import models

class Fruit(models.Model):
    fruitId = models.AutoField(primary_key=True)
    fruitAmount = models.IntegerField(default=10)

    def __str__(self):
        return f"과일 이름: fruit{self.fruitId}, 수량: {self.fruitAmount}"

    def getFruitName(self):
        return self.fruitId

    def getFruitAmount(self):
        return self.fruitAmount

    class Meta:
        db_table = "fruit"
