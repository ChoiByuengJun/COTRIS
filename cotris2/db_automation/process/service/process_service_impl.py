from process.service.process_service import ProcessService
from buyer.repository.buyer_repository_impl import BuyerRepositoryImpl
from db_automation.fruit.repository.fruit_repository_impl import FruitRepositoryImpl
from order.repository.order_repository_impl import OrderRepositoryImpl
from fruit.repository.fruit_repository_impl import FruitRepositoryImpl

class ProcessServiceImpl(ProcessService):

    __instance=None

    def __new__(cls):
        """
        구매자가 요청한 과일 개수와 우리 재고 리스트에 있는 과일 개수를 비교한다.
             1. 구매자가 요청한 과일 개수 <= 우리 재고 리스트에 있는 과일 개수
               -> 주문 가능, "주문 완료되었습니다!"
            2. 구매자가 요청한 과일 개수 > 우리 재고 리스트에 있는 과일 개수
                -> 주문 불가, "해당 과일은 현재 수량이 부족합니다ㅠㅠ"

        Arguments:
            fruit_amount: 우리 재고에 있는 과일 개수
            buyer_requirements: 구매자가 주문한 과일 개수
        """
        cls.__instance.__buyerRepository = BuyerRepositoryImpl.getInstance()
        cls.__instance.__fruitRepository = FruitRepositoryImpl.getInstance()
        cls.__instance.__orderRepository = OrderRepositoryImpl.getInstance()

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance=cls()
        
        return cls.__instance

    @classmethod
    def check_buyer_require(self, fruit_amount, buyer_requirements):
        """구매자가 주문한 과일과 우리 재고 리스트에 있는 과일 개수를 비교"""

        fruit_amount=self.__fruitRepository.createFruit.getFruitAmount()
        buyer_requirements=self.__orderRepository.order.getAmount()

        if fruit_amount >= buyer_requirements:
            print(f">>>주문이 가능합니다!<<<")
        elif fruit_amount < buyer_requirements:
            print(f">>>주문이 불가합니다!<<<")