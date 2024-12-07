from django.urls import path, include
from rest_framework.routers import DefaultRouter

from car.controller.car_controller import CarController

# 웹 브라우저에서 아래 요청에 대한 기본 URL이 /dice로 시작
router = DefaultRouter()
router.register(r"car", CarController, basename='car')

urlpatterns = [
    path('', include(router.urls)),
    path('request-crawl-car-data',
         CarController.as_view({ 'get': 'requestCrawlCarData' }),
         name='자동차 정보 크롤링'),
    path('request-car-list',
         CarController.as_view({ 'get': 'requestCarList' }),
         name='자동차 정보 리스트 획득'),
    path('request-modify-car-text',
         CarController.as_view({ 'get': 'requestModifyCarText' }),
         name='자동차 이름 변경'),
]