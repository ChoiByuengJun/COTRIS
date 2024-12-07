from car.entity.car import Car
from car.repository.car_repository import CarRepository

import pandas as pd


class CarRepositoryImpl(CarRepository):
    # 싱글턴 패턴 사용-> 싱글턴을 사용하려면 classmethod를 지정해줍니다~
    __instance = None

    def __new__(cls):
        # 싱글턴이 없다면 싱글턴을 선언해줍니다~
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    # 싱글턴 (__instance) 사용-> classmethod 지정~
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    def create(self, carData):
        # 자동차에 대한 정보를 가져옵니다.

        # carData에 저장된 정보를 가져옵니다
        car = Car(**carData)
        car.save()
        # repository 도메인에 저장~

        # 자동차에 대한 정보 반환
        return car

    # create에서 저장한 자동차에 대한 정보들을 보관할 리스트 생성~
    def createMany(self, carDataList):
        cars = []
        for carData in carDataList:
            car = Car(**carData)
            car.save()
            cars.append(car)
        return cars

    # pd.DataFrame 형식으로 반환합니다~
    # 추가적으로 pd.DataFrame으로 생성된 인스턴스는 크기 변경이 가능한 2차원 배열입니다~
    def findAll(self) -> pd.DataFrame:
        # 자동차의 모든 객체들에 대한 값들
        cars = Car.objects.all().values()
        return pd.DataFrame(cars)

    #
    def save(self, carData):
        try:
            # 데이터베이스에서 ID로 기존 레코드 검색-> 자동차 정보(carData)에 저장된 id(carData['id'])
            car = Car.objects.get(id=carData['id'])

            # 업데이트할 필드 설정-> 자동차에 대한 text를 저장~
            car.text = carData['text']

            # 저장
            car.save()
            # 자동차 id가 성공적으로 업데이트 되었습니다~
            print(f"Car with ID {car.id} successfully updated.")
            # 자동차 id(carData['id'])가 데이터베이스(carData)에 존재하지 않습니다-> 오류 발생
        except Car.DoesNotExist:
            print(f"Car with ID {carData['id']} does not exist in the database.")
            # 자동차 데이터를 저장하는 중에 오류가 발생했습니다!->
        except Exception as e:
            print(f"An error occurred while saving the car data: {e}")
