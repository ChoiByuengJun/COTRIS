from abc import ABC, abstractmethod


class CarService(ABC):

    @abstractmethod
    # 자동차 정보(CarData)를 crawl!
    def crawlCarData(self):
        pass

    @abstractmethod
    # 자동차 리스트(carList)
    def carList(self):
        pass

    @abstractmethod
    def requestModifyCarText(self):
        pass
