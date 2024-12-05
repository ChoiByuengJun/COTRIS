from django.db import models

# Create your models here.
class Buyer(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"구매자: 과일매니아{id}"

    def getId(self):
        return self.id

    class Meta:
        db_table = "buyer"