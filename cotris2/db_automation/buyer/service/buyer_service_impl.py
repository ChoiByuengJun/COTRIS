from db_automation.buyer.repository.buyer_repository_impl import BuyerRepositoryImpl
from db_automation.buyer.service.buyer_service import BuyerService


class BuyerServiceImpl(BuyerService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__buyerRepository = BuyerRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createBuyer(self, id):
        self.__buyerRepository.create(id)
