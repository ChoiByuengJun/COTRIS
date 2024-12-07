from car_registration.entity.car_registration import CarRegistration
from car_registration.repository.car_registration_repository import CarRegistrationRepository

import pandas as pd


class CarRegistrationRepositoryImpl(CarRegistrationRepository):
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

    def create(self, carRegistrationData):
        carRegistration = CarRegistration(**carRegistrationData)
        carRegistration.save()
        return carRegistration

    def createMany(self, carRegistrationDataList):
        carRegistrationList = []
        for carRegistrationData in carRegistrationDataList:
            carRegistration = CarRegistration(**carRegistrationData)
            carRegistration.save()
            carRegistrationList.append(carRegistration)

        return carRegistrationList

    def findAll(self):
        carRegistrationList = CarRegistration.objects.all().values()
        print(f"carRegistrationList: {carRegistrationList}")
        return pd.DataFrame(carRegistrationList)
