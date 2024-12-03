from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=255)  # 플레이어 이름 최대 글자수
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시간 자동 기록

    def __str__(self):
        return f"Player(name={self.name})"

    def getId(self):
        return self.id  # 모델의 기본 ID 필드 사용
