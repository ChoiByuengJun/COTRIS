import os
import pandas as pd

from car_registration.repository.car_registration_repository_impl import CarRegistrationRepositoryImpl
from car_registration.service.car_registration_service import CarRegistrationService


class CarRegistrationServiceImpl(CarRegistrationService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__carRegistrationRepository = CarRegistrationRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def __readCarTextsFromFile(self, filePath):
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

    def createCarRegistration(self):
        csvFilePath = os.path.join("resource", "car_registration.xlsx")
        currentWorkingDirectory = os.getcwd()
        absPath = os.path.join(currentWorkingDirectory, csvFilePath)

        # 파일에서 데이터를 읽는 것은 헬퍼로 위임
        carTextList = self.__readCarTextsFromFile(absPath)
        if not carTextList:
            return False

        print(f"carTextList: {carTextList}")

        for carData in carTextList:
            try:
                # '등록대수1'을 정수로 변환
                carData['등록대수1'] = int(carData['등록대수1'])
            except ValueError:
                carData['등록대수1'] = 0  # 숫자가 아니면 0으로 처리
                print(f"Invalid value for '등록대수1' in data: {carData}")

            try:
                # '등록대수2'를 실수로 변환
                carData['등록대수2'] = float(carData['등록대수2'])
            except ValueError:
                carData['등록대수2'] = 0.0  # 숫자가 아니면 0으로 처리
                print(f"Invalid value for '등록대수2' in data: {carData}")

        self.__carRegistrationRepository.createMany(carTextList)
        return True

    def carRegistrationList(self):
        return self.__carRegistrationRepository.findAll()

