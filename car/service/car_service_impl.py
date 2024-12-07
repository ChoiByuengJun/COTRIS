import os

from car.repository.car_repository_impl import CarRepositoryImpl
from car.service.car_service import CarService
from crawl.repository.crawl_repository_impl import CrawlRepositoryImpl

import re
import pandas as pd


class CarServiceImpl(CarService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            # CarRepositoryImpl에서 필요한 정보를 가져옵니다.
            cls.__instance.__carRepository = CarRepositoryImpl.getInstance()
            # CrawlRepositoryImpl에서 필요한 정보를 가져옵니다.
            cls.__instance.__crawlRepository = CrawlRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def cleanCarData(self, carData):
        cleanedData = []

        for car in carData:
            cleanedCar = {}

            # 각 예상 키를 정리
            # car.items()는 key, value를 한 번에 얻습니다.
            for key, value in car.items():
                # value(값)이 str(문자열)인가요?
                if isinstance(value, str):
                    # 필요 시 숫자가 아닌 문자를 제거 (예: '60 min' -> '60')
                    # re.sub 대신 str.replace를 사용할 수도 있습니다. 다만 둘은 차이점이 존재합니다.

                    # re.sub은 정규 표현식을 사용했습니다. r'[^0-9.]는 숫자(0-9)와 마침표(.)를 제외한 모든 문자를 매칭합니다.
                    # 즉, 정규 표현식을 활용하여 패턴 단위로 처리 가능합니다-> '123.45'

                    # 하지만, str.replace는 정규 표현식을 지원하지 않으며, 만약 str.replace를 사용하고 싶다면 하나씩 제거해야 합니다.
                    cleanedValue = re.sub(r'[^0-9.]', '', value)

                    # 필드 유형에 따라 추가로 정리할 수 있음
                    if key == 'power':
                        # 예: 'kW' 또는 'PS'와 같은 power 필드를 정리
                        # key가 "power"라면 값도 value의 불필요한 문자를 제거해줍니다.
                        cleaned_value = re.sub(r'[^0-9]', '', cleanedValue)
                    # cleandCar 딕셔너리에 불필요한 문자가 제거된 value 값을 넣어줍니다.
                    cleanedCar[key] = cleanedValue
                # value(값)이 str(문자열)이 아닌 경우 불필요한 문자를 제거해주지 않고 그냥 value 값을 넣어줍니다.
                else:
                    cleanedCar[key] = value

            # 불필요한 문자가 제거된 자동차 정보를 cleanedCar 리스트에 보관합니다~
            cleanedData.append(cleanedCar)

        return cleanedData

    # 주행 거리?를 주행 거리가 담긴 자동차 정보를 실수형으로 변환해줍니다.
    def __processDriveRange(self, carData):
        # 'drive_range' 필드 처리 (예: ' km' 제거 후 float로 변환)
        # carData['drive_range']('drive_rage'에 대한 자동차 정보가 str(문자열)이라면:
        if 'drive_range' in carData and isinstance(carData['drive_range'], str):
            # carData['drive_range']('drive_range'에 대한 자동차 정보)에서 'km'을 ''으로 바꿔주고 공백을 제거해주고(strip) 실수형(float)으로 변환합니다.
            carData['drive_range'] = float(carData['drive_range'].replace(' km', '').strip())
        return carData


    def __processEmptyFields(self, carData):
        # 빈 값 또는 유효하지 않은 값을 확인할 필드
        # 여기서 보니 '전장', '전폭', '전고', '축거'에 대해 확인을 할 것 같네요~
        fields_to_check = ['전장', '전폭', '전고', '축거']

        # carData가 딕셔너리 목록일 경우 각 딕셔너리 처리
        # carData(자동차 정보)가 리스트 형태인가요?
        if isinstance(carData, list):
            # carData(자동차 정보) 리스트에 car
            for car in carData:
                # car(자동차)가 딕셔너리 형태인가요?
                if isinstance(car, dict):
                    # '전장', '전폭', '전고', '축거'에서 해당하는 값이 있는지 대조해봅니다.
                    for field in fields_to_check:
                        # .get()을 사용하여 키가 없을 경우도 처리
                        field_value = car.get(field, None)

                        # 디버깅을 위한 현재 필드와 값 출력
                        # 예) '전장':
                        print(f"Before processing field '{field}': {field_value}")

                        # 필드가 carData에 있고 유효한 값일 경우 처리
                        if field_value is None or field_value == '' or isinstance(field_value, str) and not field_value.strip():
                            # 필드가 비어 있거나 유효하지 않은 경우(비어 있거나 부적절한) 기본값 할당 또는 처리
                            print(f"Field '{field}' is empty or invalid. Assigning default value or handling error.")
                            car[field] = -1
                        else:
                            # 필드가 유효한 경우 그대로 유지
                            print(f"Field '{field}' has valid data: {field_value}")
                # car(자동차)가 딕셔너리 형태가 아닌 경우
                else:
                    print(f"Unexpected data structure: {car} is not a dictionary")
        # carData(자동차 정보)가 리스트가 아닌 경우
        else:
            print(f"Expected carData to be a list, but got {type(carData)}")

        return carData

    def __convertRangesToNumeric(self, carData):
        # 범위 데이터를 숫자로 변환
        def parse_range(value):
            try:
                # 숫자가 아닌 문자를 제거하고 범위 분리 (예: "100-200km")
                # 리스트 컴프리핸션, 정규 표현식을 사용
                numbers = [int(x) for x in re.findall(r'\d+', value)]
                # 범위일 경우 평균값 계산, 단일 값이면 그대로 사용
                # numbers 값일 경우 평균값을 계산하지만 그 외의 값이라면 None을 반환
                return sum(numbers) // len(numbers) if numbers else None
            # 예외 처리-> parse range에 해당하는 값이 아닌 다른 값이 들어 있습니다.
            except Exception as e:
                print(f"Error parsing range: {value}, {e}")
                return None

        for car in carData:
            # car에 'drive_range'에 대한 정보가 들어 있다면
            if 'drive_range' in car:
                # parse_range의 'drive_range'에 대한 정보를 car에 기입합니다.
                car['drive_range'] = parse_range(car['drive_range'])
            # car에 'charge_time에 대한 정보가 들어 있다면
            if 'charge_time' in car:
                # parse_range의 'charge_time'에 대한 정보를 car에 기입합니다.
                car['charge_time'] = parse_range(car['charge_time'])

        # 범위 데이터를 숫자로 변환하여 저장한 carData를 반환합니다.
        return carData

    def __convertNumericFields(self, carData):
        # 숫자 필드 변환
        def parse_numeric(value):
            try:
                # value를 정수값을 반환합니다.
                return int(value)
            # value가 잘못된 값입니다-> 오류 발생(valueError)
            except ValueError:
                try:
                    # 잘못된 값이 들어있는 value를 실수형(float)으로 반환합니다.
                    return float(value)
                # 값(value)을 숫자형으로 바꾸는 과정에서 오류가 발생합니다.
                except ValueError:
                    print(f"Error converting value to numeric: {value}")
                    return None

        # carData(자동차 정보)에서 'power', '전장', '전폭', '전고', '축거'에 대한 정보를 기입합니다.
        for car in carData:
            for field in ['power', '전장', '전폭', '전고', '축거']:
                if field in car:
                    car[field] = parse_numeric(car[field])
        return carData

    # carData(자동차 정보)에 대해 필요한 정보들을 모두 크롤링해옵니다.
    def crawlCarData(self):
        carData = self.__crawlRepository.crawl()
        print(f"carData: {carData}")
        cleanedCarData = self.cleanCarData(carData)
        print(f"cleanedCarData: {cleanedCarData}")
        clearKmDriveRangeData = self.__processDriveRange(cleanedCarData)
        print(f"clearKmDriveRangeData: {clearKmDriveRangeData}")
        clearDataWithEmptyFieldsProcessed = self.__processEmptyFields(clearKmDriveRangeData)
        print(f"clearDataWithEmptyFieldsProcessed: {clearDataWithEmptyFieldsProcessed}")
        numericConvertedData = self.__convertRangesToNumeric(clearDataWithEmptyFieldsProcessed)
        print(f"numericConvertedData: {numericConvertedData}")
        fullyProcessedData = self.__convertNumericFields(numericConvertedData)
        print(f"fullyProcessedData: {fullyProcessedData}")
        createdCar = self.__carRepository.createMany(numericConvertedData)

        # createdCar가 빈 값이 아니라면 참(True)을 반환합니다.
        if createdCar is not None:
            return True

        # else createdCar is None:
        return False

    # carRepository(자동차 레파지토리)에 있는 값들을 모두(findAll()) 찾아옵니다.
    def carList(self):
        return self.__carRepository.findAll()

    # 경로(resource)와 파일명(car_text_modify.csv)을 결합합니다(os.path.join)
    def requestModifyCarText(self):
        csvFilePath = os.path.join("resource", "car_text_modify.csv")

        # 파일에서 데이터를 읽는 것은 헬퍼로 위임
        carTextList = self.__readCarTextsFromFile(csvFilePath)
        if not carTextList:
            return

        print(f"carTextList: {carTextList}")

        # 기존 데이터 가져오기
        existingCarList = self.__carRepository.findAll()
        print(f"existingCarList: {existingCarList}")

        # 기존 데이터와 파일 데이터를 기반으로 업데이트 작업만 수행
        updateCarList = self.__prepareUpdateCars(existingCarList, carTextList)
        print(f"updateCarList: {updateCarList}")

        # 업데이트 작업 실행
        if updateCarList:
            self.__updateExistingCars(updateCarList)
            return True

        print("업데이트할 데이터가 없습니다.")
        return False

    # Private Method 1: 파일에서 텍스트 읽기
    def __readCarTextsFromFile(self, csvFilePath):
        currentWorkingDirectory = os.getcwd()   # csv 파일을 호출합니다.
        print(f"현재 작업 디렉토리: {currentWorkingDirectory}")

        # 절대 경로 생성
        absPath = os.path.join(currentWorkingDirectory, csvFilePath)
        print(f"absPath: {absPath}")

        if not os.path.exists(absPath):
            print(f"CSV 파일이 존재하지 않습니다: {absPath}")
            return None

        try:
            with open(absPath, newline="", encoding="utf-8") as csvfile:
                # 첫 번째 줄을 건너뛰고 데이터를 읽어들임
                reader = csvfile.readlines()[1:]  # 첫 번째 줄을 건너뛰고 나머지 데이터를 읽음
                return {line.strip() for line in reader if line.strip()}  # 빈 줄을 제외하고 데이터만 셋에 추가
        except Exception as e:
            print(f"CSV 파일을 읽는 중 오류 발생: {e}")
            return None

    # Private Method 2: 업데이트 데이터 준비
    def __prepareUpdateCars(self, existingCarList, carTextList):
        update_cars = []
        print(f'len(existingCarList): {len(existingCarList)}')
        print(f'len(carTextList): {len(carTextList)}')

        # carTextList가 빈 값이 아니어야 함
        if carTextList:
            # existingCarList의 각 항목에 대해 carTextList에서 값을 가져와서 넣기
            carTextList = list(carTextList)  # set이 아닌 list로 변환 (순서 보장)

            if len(existingCarList) == len(carTextList):
                for i, car in enumerate(existingCarList.to_dict("records")):
                    car['text'] = carTextList[i]  # carTextList에서 해당 인덱스의 값을 넣기
                    update_cars.append({"id": car["id"], "text": car['text']})
                    print(f"Updated car with id: {car['id']} and new text: {car['text']}")
            # carTextList의 길이와 existingCarList의 길이가 맞지 않습니다.
            else:
                print("The lengths of existingCarList and carTextList do not match.")
        else:
            print("carTextList is empty.")

        return update_cars

    # Private Method 3: 기존 데이터 업데이트
    def __updateExistingCars(self, updateCarList):
        for carData in updateCarList:
            self.__carRepository.save(carData)
            print(f"업데이트된 차량 데이터: {carData['text']}")
