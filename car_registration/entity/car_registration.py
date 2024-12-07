from django.db import models

class CarRegistration(models.Model):
    # 자동차를 등록하기 위해 필요한 정보들이 담겨 있는 테이블이겠네요~
    # id를 CarRegistration 테이블의 기본키로 지정했습니다.
    id = models.AutoField(primary_key=True)
    지역1 = models.CharField(max_length=50, null=True, blank=True)
    등록대수1 = models.IntegerField(null=True, blank=True)
    등록대수2 = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.지역1} - {self.등록대수1}"

    class Meta:
        db_table = 'car_registration'
