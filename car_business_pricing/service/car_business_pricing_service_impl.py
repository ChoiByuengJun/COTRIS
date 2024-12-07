import os

from car_business_pricing.repository.car_business_pricing_repository_impl import CarBusinessPricingRepositoryImpl
from car_business_pricing.service.car_business_pricing_service import CarBusinessPricingService

import pandas as pd


class CarBusinessPricingServiceImpl(CarBusinessPricingService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__carBusinessPricingRepository = CarBusinessPricingRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def __readBusinessPricingTextsFromFile(self, filePath):
        try:
            # 엑셀 파일 읽기
            df = pd.read_excel(filePath)

            # 데이터가 잘 읽혔는지 확인
            print(df.head())  # 확인을 위해 첫 번째 5개 데이터 출력

            # 데이터프레임을 리스트로 변환
            carTextList = df.to_dict(orient='records')
            return carTextList

        except Exception as e:
            print(f"파일을 읽는 중 오류가 발생했습니다: {str(e)}")
            return []

    def createCarBusinessPricing(self):
        csvFilePath = os.path.join("resource", "car_business_pricing.xlsx")
        currentWorkingDirectory = os.getcwd()
        absPath = os.path.join(currentWorkingDirectory, csvFilePath)

        # 파일에서 데이터를 읽는 것은 헬퍼로 위임
        carBusinessPricingList = self.__readBusinessPricingTextsFromFile(absPath)
        if not carBusinessPricingList:
            return False

        print(f"carBusinessPricingList: {carBusinessPricingList}")

        try:
            df = pd.DataFrame(carBusinessPricingList)
            df = df.fillna(0.0)  # NaN 값을 0.0으로 변환
            cleanedCarBusinessPricingList = df.to_dict(orient="records")  # 다시 리스트로 변환
            print(f"변환된 carBusinessPricingList: {cleanedCarBusinessPricingList}")

            # 데이터베이스에 저장
            createdRecords = self.__carBusinessPricingRepository.createMany(cleanedCarBusinessPricingList)
            print(f"총 {len(createdRecords)}개의 데이터가 저장되었습니다.")
            return True

        except Exception as e:
            print(f"데이터 저장 중 오류가 발생했습니다: {str(e)}")
            return False

    def carBusinessPricingList(self):
        return self.__carBusinessPricingRepository.findAll()

