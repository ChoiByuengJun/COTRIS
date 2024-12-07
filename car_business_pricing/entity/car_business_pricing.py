from django.db import models

class CarBusinessPricing(models.Model):
    # 자동차 비즈니스에 필요한 가격 정보들이 있네요~(id, 사업자, 로밍평균요금, 회원평균요금, 비회원평균요금)
    # id를 car_business_pricing 테이블의 기본키(primary_key로 지정해주었습니다)
    id = models.AutoField(primary_key=True)
    사업자 = models.CharField(max_length=50, null=True, blank=True)
    로밍평균요금 = models.FloatField(null=True, blank=True)
    회원평균요금 = models.FloatField(null=True, blank=True)
    비회원평균요금 = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.사업자} Pricing"

    class Meta:
        db_table = 'car_business_pricing'
