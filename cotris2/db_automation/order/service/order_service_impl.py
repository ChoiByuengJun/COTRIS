from order.repository.order_repository_impl import OrderRepositoryImpl
from order.service.order_service import OrderService


class OrderServiceImpl(OrderService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            # cls.__instance.__buyerRepository = BuyerRepositoryImpl.getInstance()
            # cls.__instance.__fruitRepository = FruitRepositoryImpl.getInstance()
            cls.__instance.__orderRepository = OrderRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def orderFruit(self, buyer, fruit):
        buyer = self.__buyerRepository.getId()
        fruit = self.__fruitRepository.getId()
        return self.__orderRepository.order(buyer, fruit)

    def findBuyer(self):
        pass
