from django.forms import model_to_dict


from db_automation.buyer.entity.buyer import Buyer
from db_automation.buyer.repository.buyer_repository import BuyerRepository

class BuyerRepositoryImpl(BuyerRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

    def create(self):
        buyer = Buyer(self)
        buyer.save()

        return model_to_dict(buyer)