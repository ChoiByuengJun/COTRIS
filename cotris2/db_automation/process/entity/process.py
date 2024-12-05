from django.db import  models
import  random


# Create my model here.
class Process(models.Model):
    fruit_id=models.AutoField(primary_key=True) # fruit_id: 과일의 id
    buyer_id=models.AutoField(primary_key=True) # buyer_id: 구매자의 id
    fruit_amount=models.IntegerField(random.randint(9, 11))  # 우리 재고에 있는 과일 수
    buyer_requirements=models.IntegerField(default=2)    # 구매자가 요청한 과일 수

    def __str__(self):
        return (
            f"fruit_id: {self.fruit_id}, buyer_ud: {self.buyer_id}, fruit_amount: {self.fruit_amount}, buyer_requirements: {self.buyer_requirements}"
        )