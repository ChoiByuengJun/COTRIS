from django.db import models

from fruit.entity.fruit import Fruit
# Create your models here.
from order.entity.order import Order


# Create my model here.
class Process(models.Model):
    id = models.AutoField(primary_key=True)
    requestedAmount = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    fruitAmount = models.ForeignKey(Fruit, on_delete=models.CASCADE, related_name='process')

    def __str__(self):
        return (
            f"재고에 있는 과일 개수: {self.fruitAmount}, 주문한 개수: {self.requestedAmount}"
        )
    
    def getFruitAmount(self):
        return self.fruitAmount
    
    def getBuyerRequirements(self):
        return self.requestedAmount
    
    def getId(self):
        return self.id

    class Meta:
        db_table="process"