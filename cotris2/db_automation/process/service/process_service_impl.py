import  random
from django.db import  models
from db_automation.process.service.process_service import ProcessService

class ProcessServiceImpl(ProcessService):

    def __init__(self, fruit_id, buyer_id, fruit_amount, buyer_requirements):
        """
        구매자가 요청한 과일 개수와 우리 재고 리스트에 있는 과일 개수를 비교한다.
             1. 구매자가 요청한 과일 개수 <= 우리 재고 리스트에 있는 과일 개수
               -> 주문 가능, "주문 완료되었습니다!"
            2. 구매자가 요청한 과일 개수 > 우리 재고 리스트에 있는 과일 개수
                -> 주문 불가, "해당 과일은 현재 수량이 부족합니다ㅠㅠ"

        Arguments:
            fruit_id: 과일의 id
            buyer_id: 구매자의 id
            fruit_amount: 우리 재고에 있는 과일 개수
            buyer_requirements: 구매자가 주문한 과일 개수
        """
        self.fruit_id=models.AutoField(primary_key=True)
        self.buyer_id=models.AutoField(primary_key=True)
        self.fruit_amount=random.randint(9, 11)
        self.buyer_requirements=random.randint(9, 11)

    def append_fruit_list(self, fruit_id, fruit_amount):
        """fruit_id를 생성과 동시에 리스트에 담아 관리합니다"""
        for i in self.fruit_amount:
            fruit_list = []
            fruit_list.append(i)
        return fruit_list

    def append_buyer_list(self, buyer_id, buyer_requirements):
        """buyer_id를 생성과 동시에 리스트에 담아 관리합니다."""
        buyer_list=[]
        for i in self.buyer_requirements:
            buyer_list.append(i)
        return buyer_list

    def check_buyer_require(self, fruit_id, buyer_id, fruit_amount, buyer_requirements):
        """구매자가 주문한 과일과 우리 재고 리스트에 있는 과일 개수를 비교"""


        if fruit_id in