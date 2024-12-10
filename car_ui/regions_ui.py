import streamlit as st
import plotly.express as px

from regions.domain.usecase import GetRegionDataUseCase
from regions.infra.car_region_repository_impl import CarRegionRepositoryImpl


def showRegionsUi():
    st.header("지역별 전기차 등록 대수 현황")
    region_repo = CarRegionRepositoryImpl()
    usecase = GetRegionDataUseCase(region_repo)

    try:
        df = usecase.execute()
        # key: 기존 칼럼명, value: 변경할 칼럼명
        # 각각 "지역1"-> "region"으로, "등록대수1"-> "count"로, "등록대수2"-> "ratio"로 바꿉니다.
        # inplace가 기본 False로 지정되어 있기 때문에 원본 변수명도 바꿔주고 싶다면 inplace=True로 지정해줍니다.
        df.rename(columns={"지역1": "region", "등록대수1": "count", "등록대수2": "ratio"}, inplace=True)

        st.write("execute() 결과 데이터프레임:")
        st.dataframe(df, use_container_width=True, height=600)

        # columns를 통해 col1, col2는 각각 2와 3의 비율로 열이 생성됩니다.
        col1, col2 = st.columns([2, 3])
        with col1:
            # table의 첫 10행을 출력합니다.
            st.table(df.head(10))
        with col2:
            # "region" 열의 값을 레이블로 사용, "ratio" 열의 값을 기준으로 크기를 계산, 도넛 차트를 빈 공간 비율을 0.3으로 지정하여 생성합니다.
            fig = px.pie(df, names="region", values="ratio", hole=0.3)
            # update_traces-> 파이 차트의 텍스트 위치와 표시 형식을 지정합니다.
            # "inside"-> 텍스트를 차트 안쪽에 배치, "percent+label"-> 퍼센트와 레이블을 함께 표시
            fig.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(fig)

    except Exception as e:
        st.error(f"지역 데이터를 불러오지 못했습니다: {e}")
