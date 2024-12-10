import streamlit as st

from charging.domain.usecase import GetChargingFeesUseCase
from charging.infra.car_charging_repository_impl import CarChargingRepositoryImpl


def showChargingUi():
    st.header("업체 별 전기차 충전 요금")
    charging_repo = CarChargingRepositoryImpl()
    usecase = GetChargingFeesUseCase(charging_repo)

    try:
        df = usecase.execute()

        st.table(df)

    except Exception as e:
        st.error(f"충전 요금 데이터를 불러오지 못했습니다: {e}")
