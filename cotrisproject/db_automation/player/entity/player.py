from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=255)  # 플레이어 이름 최대 글자수
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Player id: {self.id}, name: {self.name})"

    def getId(self):
        return self.id  # 모델의 기본 ID 필드 사용

