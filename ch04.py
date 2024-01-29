# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly

@st.cache_data
def load_data():
    df = sns.load_dataset('tips')
    return df

def main():
    # st.write(mpl.__version__)
    st.write("Streamlit with Maplotlib")
    tips = load_data()

    # 시각화 아무거나 만들기
    # plt.show() 기존에 쓰던 시각화 명령어. 그런데 여기선 다르다.
    # 사용 st.pyplot(fig)

    # 데이터가공
    m_tips = tips.loc[tips['sex'] == 'Male', :]
    f_tips = tips.loc[tips['sex'] == 'Female', :]
    # 시각화 차트
    fig, ax = plt.subplots(ncols=2, figsize=(10, 6), sharex=True, sharey=True)
    ax[0].scatter(x = m_tips['total_bill'], y = m_tips['tip'])
    ax[0].set_title('Male')
    ax[1].scatter(x = f_tips['total_bill'], y = f_tips['tip'])
    ax[1].set_title('Female')
    st.pyplot(fig)



    # 이번에는 seaborn으로 시각화 코드 아무거나 작성(진짜 아무거나 작성해본 것.)
    fig, ax = plt.subplots()

    # Seaborn의 내장 데이터셋인 'tips' 로드
    tips = sns.load_dataset("tips")

    # 산점도(Scatter Plot) 그리기
    sns.scatterplot(x="total_bill", y="tip", data=tips, hue="sex", style="time")

    # 그래프에 제목 추가
    plt.title("Scatter Plot of Total Bill vs Tip")


    st.pyplot(fig)

    # 이하는 받은 것.(seaborn)

    fig, ax = plt.subplots(ncols=2, figsize=(10, 6), sharex=True, sharey=True)
    sns.scatterplot(data=m_tips, x = 'total_bill', y = 'tip', ax=ax[0])
    ax[0].set_title('Male')
    sns.scatterplot(data=f_tips, x = 'total_bill', y = 'tip', ax=ax[1])
    ax[0].set(xlabel=None, ylabel=None)
    ax[1].set_title('Female')
    ax[1].set(xlabel=None, ylabel=None)
    
    st.pyplot(fig)


    # plotly로 차트 만들기

    fig = px.line(tips, x='day', y='total_bill', title='Plotly Line Chart')

    st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(tips, x='day', y='total_bill', title='Plotly Bar Chart')

    st.plotly_chart(fig, use_container_width=True)

    # 이건 강사님의 plotly 차트

    fig = make_subplots(rows = 1,
                    cols = 2,
                    subplot_titles=('Male', 'Female'),
                    shared_yaxes=True,
                    shared_xaxes=True,
                    x_title='Total Bill($)'
                    )
    fig.add_trace(go.Scatter(x = m_tips['total_bill'], y = m_tips['tip'], mode='markers'), row=1, col=1)
    fig.add_trace(go.Scatter(x = f_tips['total_bill'], y = f_tips['tip'], mode='markers'), row=1, col=2)
    fig.update_yaxes(title_text="Tip($)", row=1, col=1)
    fig.update_xaxes(range=[0, 60])
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

    # 스트림릿에서는 plotly를 이용한 시각화가 더 낫다고 한다. 차트에 마우스를 댔을 때 데이터 정보가 표시되는 것은 plotly. 그래서 더 좋음.
    # 이는 해당 코드를 streamlit run 해서 그래프에 마우스를 대보면 바로 알 수 있다.




if __name__ == "__main__":
    main()