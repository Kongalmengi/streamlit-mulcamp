# -*- coding:utf-8 -*- 요 주석은 한글주석이 깨질 수 있기 때문에 넣는다 함.

import streamlit as st
import seaborn as sns
import pandas as pd

@st.cache_data # decorator, 함수의 중급레벨 사용법. 이건 따로 공부하는 것이 좋다.
# 참고로 위의 코드는 캐시데이터를 쓴다는 의미라고 함. 이와 관련된 내용은 슬라이드에 찾아보면 있음.
def load_data():
    df = sns.load_dataset("tips")
    return df # 이 리턴값이 없으면 결과가 안나옴.

def main():
    st.write(st.__version__)
    st.write(sns.__version__)
    st.write(pd.__version__)

    tips = load_data()
    st.dataframe(tips, use_container_width=True)
    
    st.write("-" * 50)
    st.title("st.metric()")
    tip_max = tips['tip'].max() # 최대값
    tip_min = tips['tip'].min() # 최소값

    st.metric(label="팁 최고금액", value=tip_max, delta = tip_max - tip_min)
    st.metric(label="팁 최소금액", value=tip_min, delta = tip_min - tip_max)

if __name__ == "__main__":
    main()