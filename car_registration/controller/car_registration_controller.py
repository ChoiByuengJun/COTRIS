from django.http import JsonResponse
from rest_framework import viewsets, status

from car_registration.service.car_registration_service_impl import CarRegistrationServiceImpl


class CarRegistrationController(viewsets.ViewSet):
    __carRegistrationService = CarRegistrationServiceImpl.getInstance()

    def requestCreateCarRegistrationData(self, request):
        isSuccess = self.__carRegistrationService.createCarRegistration()

        return JsonResponse({'success': isSuccess})

    def requestCarRegistrationList(self, request):
        try:
            carRegistrationListDataFrame = self.__carRegistrationService.carRegistrationList()
            print(f"carRegistrationListDataFrame: {carRegistrationListDataFrame}")

            return JsonResponse(carRegistrationListDataFrame.to_dict(orient='records'), safe=False)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

