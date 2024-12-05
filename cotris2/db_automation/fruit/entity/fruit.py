from django.db import models

class Fruit(models.Model):
    fruitId = models.AutoField(primary_key=True)
    fruitNum = models.IntegerField(default=10)

    def __str__(self):
        return f"과일 id: {self.id}, 수량: {self.}"


