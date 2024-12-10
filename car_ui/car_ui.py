# asyncio는 async/await 구문을 사용하여 동시성 코드를 작성할 수 있게 해주는 모듈로, 
# asyncio를 사용하면 단일 스레드 작업을 병렬로 처리할 수 있다.

"""
# asyncio를 사용하지 않은 예

def sum(name, numbers):
    start = time.time()
    total = 0
    for number in numbers:
        sleep()
        total += number
        print(f'작업중={name}, number={number}, total={total}')
    end = time.time()
    print(f'작업명={name}, 걸린시간={end-start}')
    return total


def main():
    start = time.time()

    result1 = sum("A", [1, 2])
    result2 = sum("B", [1, 2, 3])

    end = time.time()
    print(f'총합={result1+result2}, 총시간={end-start}')
"""

"""
# asyncio 사용한 예-> def 앞에 async를 선언하면 된다(코루틴)

async def sum(name, numbers):
    start = time.time()
    total = 0
    for number in numbers:
        await sleep()
        total += number
        print(f'작업중={name}, number={number}, total={total}')
    end = time.time()
    print(f'작업명={name}, 걸린시간={end-start}')
    return total


async def main():
    start = time.time()

    task1 = asyncio.create_task(sum("A", [1, 2]))
    task2 = asyncio.create_task(sum("B", [1, 2, 3]))

    await task1
    await task2

    result1 = task1.result()
    result2 = task2.result()
"""
import asyncio 

import streamlit as st

from cars.domain.usecase import GetCarsUseCase
from cars.infra.car_repository_impl import CarRepositoryImpl

# 코루틴
async def showCarUi():
    # CarRepositoryImpl(), GetCarUseCase()를 가져옵니다.
    car_repo = CarRepositoryImpl()
    usecase = GetCarsUseCase(car_repo)

    try:
        # usecase를 실행합니다.
        df = usecase.execute()
        
        # header-> 제목이 아닙니다/ 제목은 st.title()로 지정해줍니다.
        st.header("전체 데이터 예시")
        # table-> usecase를 table로 보여줍니다.
        st.table(df)

    # excute할 usecase를 불러오지 못했다는 뜻이겠죠~
    except Exception as e:
        st.error(f"차량 데이터를 불러오지 못했습니다: {e}")