from django.http import JsonResponse
from rest_framework import viewsets, status

from car_business_pricing.service.car_business_pricing_service_impl import CarBusinessPricingServiceImpl


class CarBusinessPricingController(viewsets.ViewSet):
    __carBusinessPricingService = CarBusinessPricingServiceImpl.getInstance()

    def requestCreateCarBusinessPricing(self, request):
        isSuccess = self.__carBusinessPricingService.createCarBusinessPricing()

        return JsonResponse({'success': isSuccess})

    def requestCarBusinessPricingList(self, request):
        try:
            carBusinessPricingListDataFrame = self.__carBusinessPricingService.carBusinessPricingList()
            print(f"carRegistrationListDataFrame: {carBusinessPricingListDataFrame}")

            return JsonResponse(carBusinessPricingListDataFrame.to_dict(orient='records'), safe=False)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

