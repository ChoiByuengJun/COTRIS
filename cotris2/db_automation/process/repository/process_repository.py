from abc import ABC, abstractmethod


class ProcessRepository(ABC):

    @abstractmethod
    def process(self, fruit_amount, buyer_requirements):
        pass