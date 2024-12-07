from django.urls import path, include
from rest_framework.routers import DefaultRouter

from car_registration.controller.car_registration_controller import CarRegistrationController

router = DefaultRouter()
router.register(r"car-registration", CarRegistrationController, basename='car')

urlpatterns = [
    path('', include(router.urls)),
    path('request-create-car-registration-data',
         CarRegistrationController.as_view({ 'get': 'requestCreateCarRegistrationData' }),
         name='자동차 등록 정보 생성'),
    path('request-car-registration-list',
         CarRegistrationController.as_view({ 'get': 'requestCarRegistrationList' }),
         name='자동차 등록 정보 리스트 획득'),
]