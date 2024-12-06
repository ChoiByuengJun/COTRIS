from django.db import models

# Create your models here.
from order.entity.order import Order


# Create my model here.
class Process(models.Model):
    fruit_amount=models.AutoField(primary_key=True)
    buyer_requirements=models.AutoField(primary_key=True)
    id=models.ForeignKey(Order, on_delete=models.CASCADE, related_name="process")
    amount=models.ForeignKey(Order, on_delete=models.CASCADE, related_name="process")

    def __str__(self):
        return (
            f"재고에 있는 과일 개수: {self.fruit_amount}, 주문한 개수: {self.buyer_requirements}"
        )
    
    def get_fruit_amount(self):
        return self.fruit_amount
    
    def get_buyer_requirements(self):
        return self.buyer_requirements
    
    def get_id(self):
        return self.id
    
    def get_amount(self):
        return self.amount
    
    class Meta:
        db_table="process"