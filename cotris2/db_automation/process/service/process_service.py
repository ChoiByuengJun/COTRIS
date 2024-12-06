from abc import ABC, abstractmethod


class ProcessService(ABC):

    @abstractmethod
    def check_buyer_require(self):
        """구매자가 요구하는 과일 개수와 리스트에 있는 과일 개수 비교"""
        pass