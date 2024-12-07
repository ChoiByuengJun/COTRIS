from car_business_pricing.entity.car_business_pricing import CarBusinessPricing
from car_business_pricing.repository.car_business_pricing_repository import CarBusinessPricingRepository

import pandas as pd


class CarBusinessPricingRepositoryImpl(CarBusinessPricingRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, carBusinessPricingData):
        # 키워드 인수 언패킹이란 것을 사용했는데, 쉽게 말해서 carBusinessPricingData 딕셔너리에 저장된 키-값 쌍을
        # CarBusinessPricing 함수에 전달합니다.
        carBusinessPricing = CarBusinessPricing(**carBusinessPricingData)
        carBusinessPricing.save()
        return carBusinessPricing

    def createMany(self, carBusinessPricingDataList):
        carBusinessPricingList = []
        for carBusinessPricingData in carBusinessPricingDataList:
            # 여기서도 키워드 인수 언패킹을 사용했네요~(**carBusinessPricingData)
            carBusinessPricing = CarBusinessPricing(**carBusinessPricingData)
            carBusinessPricing.save()
            carBusinessPricingList.append(carBusinessPricing)

        return carBusinessPricingList

    def findAll(self):
        # all().values()-> 모든 값들을 가져오네요.
        carBusinessPricingList = CarBusinessPricing.objects.all().values()
        print(f"carBusinessPricingList: {carBusinessPricingList}")
        # pandas의 DataFrame 형태로 반환합니다.
        # 이때 반환 carBusinessPricingList가 반환되는 형태는 carBusinessPricingList의 형태에 따라 달라지게 됩니다.
        # 리스트인 경우, 리스트의 리스트인 경우, 단일 딕셔너리, 단일 리스트인 경우에 따라 반환되는 형태가 달리집니다.
        return pd.DataFrame(carBusinessPricingList)
