from django.db import models

# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE, related_name='order')
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='order')

    def __str__(self):
        return f"주문자 id: {self.buyer}, 주문한 과일: {self.fruit}, 주문한 개수: {self.amount}"

    def getId(self):
        return self.id

    def getAmount(self):
        return self.amount

    def getFruit(self):
        return self.fruit

    def getBuyer(self):
        return self.buyer

    class Meta:
        db_table = "order"

