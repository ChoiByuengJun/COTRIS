from fruit.entity.fruit import Fruit
from fruit.repository.fruit_repository import FruitRepository


class FruitRepositoryImpl(FruitRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

    def createFruit(self):
        fruitList = []

        for _ in range(3):
            fruit = Fruit()  # Fruit 객체 생성 후 데이터베이스에 저장
            print(f"과일 id: {fruit.fruitId}, 수량: {fruit.fruitAmount}")

            fruit = Fruit(self)
            fruit.save()

            fruitList.append(fruit)

        return fruitList

    def findById(self, id):
        return Fruit.objects.get(id=id)
    