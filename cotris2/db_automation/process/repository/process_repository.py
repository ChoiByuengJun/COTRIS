from abc import ABC, abstractmethod


class ProcessRepository(ABC):

    @abstractmethod
    def per_nums_buyers_and_list(self, requirements, amount):
        """requirements: 구매자 요구 과일 개수", amount: 리스트에 있는 과일 개수"""
        pass