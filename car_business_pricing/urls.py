from django.urls import path, include
from rest_framework.routers import DefaultRouter

from car_business_pricing.controller.car_business_pricing_controller import CarBusinessPricingController

router = DefaultRouter()
router.register(r"car-business-pricing", CarBusinessPricingController, basename='car_business_pricing')

urlpatterns = [
    path('', include(router.urls)),
    path('request-create-car-business-pricing',
         CarBusinessPricingController.as_view({ 'get': 'requestCreateCarBusinessPricing' }),
         name='자동차 요금 정보 생성'),
    path('request-car-business-pricing-list',
         CarBusinessPricingController.as_view({ 'get': 'requestCarBusinessPricingList' }),
         name='자동차 요금 정보 리스트 획득'),
]