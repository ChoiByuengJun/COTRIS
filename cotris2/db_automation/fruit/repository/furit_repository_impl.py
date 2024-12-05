from fruit.entity.fruit import Fruit

# 과일 데이터 생성
fruits = [
    Fruit(fruitId=1, fruitNum=10),
    Fruit(fruitId=2, fruitNum=10),
    Fruit(fruitId=3, fruitNum=10),
]

# 데이터베이스에 저장
for fruit in fruits:
    fruit.save()
