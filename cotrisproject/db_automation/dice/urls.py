from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dice.controller.dice_controller import DiceController

# 웹 브라우저에서 아래 요청에 대한 기본 URL이 /dice로 시작
router = DefaultRouter()
router.register(r"dice", DiceController, basename='dice')

urlpatterns = [
    path('', include(router.urls)),
    path('request-roll-dice', 
         # 웹 브라우저 상에서 /request-roll-dice 요청이 오면 'requestRollDice()' 구동
         # 결론적으로 /dice/request-roll-dice 로 시작
         DiceController.as_view({ 'get': 'requestRollDice' }),
         name='주사위 굴리기'),
    path('request-find-dice',
         DiceController.as_view({ 'get': 'requestFindDice' }),
         name='주사위 id로 찾기'),
    path('request-every-dice',
         DiceController.as_view({ 'get': 'requestEveryDice' }),
         name='주사위 전체 정보 획득'),
]