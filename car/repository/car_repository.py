from abc import ABC, abstractmethod
import pandas as pd


class CarRepository(ABC):

    @abstractmethod
    # 생성?
    def create(self, carData):
        pass

    @abstractmethod
    # 찾아준다?
    def findAll(self) -> pd.DataFrame:
        pass

    @abstractmethod
    # 저장하고~
    def save(self, carData):
        pass
