import streamlit as st

from cars.presentation.car_ui import showCarUi
from charging.presentation.charging_ui import showChargingUi
from regions.presentation.regions_ui import showRegionsUi

st.set_page_config(layout="wide")
st.title("전기차 종합 DB 조회 포털:mag:")

tab1, tab2, tab3 = st.tabs(["차량 정보 조회", "전기차 등록 대수 현황", "업체 별 전기차 충전 요금"])

with tab1:
    # "차량 정보 조회" 탭을 누르면 CarUi에 대한 정보가 나오겠군요~
    showCarUi()

with tab2:
    # "전기차 등록 대수 현황" 탭을 누르면 RegiosUi에 대한 정보가 나오겠군요~
    showRegionsUi()

with tab3:
    # "업체 별 전기차 충전 요금" 탭을 누르면 ChargingUi에 대한 정보가 나오겠군요~
    showChargingUi()
