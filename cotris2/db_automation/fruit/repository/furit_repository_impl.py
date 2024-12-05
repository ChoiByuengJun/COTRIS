from fruit.furit_repository import FruitRepository
from fruit.entity.fruit import Fruit

class CreateFruit(FruitRepository):
    def createFruit(self):
        for _ in range(3):
            fruit = Fruit.objects.create()  # Fruit 객체 생성 후 데이터베이스에 저장
            print(f"과일 id: {fruit.Id}, 수량: {fruit.fruitNum}")


