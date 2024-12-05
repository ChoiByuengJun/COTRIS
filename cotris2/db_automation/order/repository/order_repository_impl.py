import random

from django.forms import model_to_dict

from order.entity.order import Order
from order.repository.order_repository import OrderRepository


class OrderRepositoryImpl(OrderRepository):
    __instance = None

    MIN = 9
    MAX = 11

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def order(self, fruit, buyer):
        fruitAmount = random.randint(self.MIN, self.MAX)
        order = Order(amount=fruitAmount, fruit=fruit, buyer=buyer)
        order.save()

        return model_to_dict(order)