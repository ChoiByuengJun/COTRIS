import random

from django.forms import model_to_dict

from process.entity.process import Process
from process.repository.process_repository import ProcessRepository

class ProcessRepositoryImpl(ProcessRepository):
    __instance=None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance=super().__new__(cls)
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance=cls()
        
        return cls.__instance
    
    def process(self, fruit_amount, buyer_requirements):
        fruitAmount = random.randint(fruit_amount, buyer_requirements)
        buyerRequirements = Process(fruit_amount=fruitAmount, buyer_requirements=fruitAmount, buyer_requirements=buyer_requirements)
        process.save()

        return model_to_dict(process)