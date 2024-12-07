from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status

from car.service.car_service_impl import CarServiceImpl


class CarController(viewsets.ViewSet):
    __carService = CarServiceImpl.getInstance()

    # CarData(자동차 정보)의 크롤링을 요청합니다.
    def requestCrawlCarData(self, request):
        isSuccess = self.__carService.crawlCarData()

        return JsonResponse({'success': isSuccess})

    # CarList(자동차 정보 리스트)를 요청합니다.
    def requestCarList(self, request):
        try:
            carListDataFrame = self.__carService.carList()
            print(f"carListDataFrame: {carListDataFrame}")

            # carListDataFrame을 딕셔너리 형태로 반환합니다.
            return JsonResponse(carListDataFrame.to_dict(orient='records'), safe=False)

        except Exception as e:
            # JsonResponse 실행 시 request(요청)이 양호하지 못하는 오류가 발생합니다.-> HTTP_400_BAD_REQUEST
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def requestModifyCarText(self, request):
        isSuccess = self.__carService.requestModifyCarText()

        if isSuccess:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Failed to modify car text'},
                                status=status.HTTP_400_BAD_REQUEST)

