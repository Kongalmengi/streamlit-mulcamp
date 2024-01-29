# -*- coding:utf-8 -*-
import streamlit as st 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
@st.cache_data
def cal_sales_revenue(price, total_sales):
    revenue = price * total_sales
    return revenue
# 데이터 불러오기
@st.cache_data
def load_data():
    df = sns.load_dataset('iris')
    return df
def plot_matplotlib(df):
    st.title('Scatter Plot with Matplotlib')
    fig, ax = plt.subplots()
    ax.scatter(df['sepal_length'], df['sepal_width'])
    st.pyplot(fig)
def plot_seaborn(df):
    st.title('Scatter Plot with Seaborn')
    fig, ax = plt.subplots()
    sns.scatterplot(df, x = 'sepal_length', y = 'sepal_width')
    st.pyplot(fig)
def plot_plotly(df):
    st.title('Scatter Plot with Plotly')
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x = df['sepal_length'],
                   y = df['sepal_width'],
                   mode='markers')
    )
    st.plotly_chart(fig)



def main():
    st.title("Button Widget")
    price = st.slider("단가:", 100, 10000, value = 5000)
    total_sales = st.slider("전체 판매 갯수:", 1, 1000, value = 500)

    st.write(price, total_sales)

    if st.button("매출액 계산"):
        revenue = cal_sales_revenue(price, total_sales)
        st.write(revenue)

    st.title("Check Box Control")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    show_plot = st.checkbox("시각화 보여주기")
    st.write(show_plot)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    if show_plot: # 체크박스가 클릭이 되면 시각화를 보여준다는 의미.
        st.pyplot(fig)
    else:
        st.write("안녕, ")

    st.title("라이브러리 선택")
    iris = load_data()
    st.data_editor(iris) # 권장 / 내일 오후 시간에도 적용 및 공부해보자.

    plot_type = st.radio(
        "어떤 스타일의 산점도를 보고 싶은가요?",
        ("Matplotlib", "Seaborn", "Plotly")
    )


    # 메서드 3개 존재
    # 조건문 사용해서, 각 radio 선택 시, 해당 시각화 메서드 호출해서 보여주기

    if plot_type == "Matplotlib":
        plot_matplotlib(iris) # 앞서 설정된 것을 불러온다.
    elif plot_type == "Seaborn":
        plot_seaborn(iris) # 앞서 설정된 것을 불러온다.
    elif plot_type == "Plotly":
        plot_plotly(iris) # 앞서 설정된 것을 불러온다.
    else:
        st.write("으악")


    st.title("SelectBox 사용")
    
    # 행 추출
    st.write(iris.species.unique()) # 어떤 항목이 있는지 알아보기 위해 써봄.
    val = st.selectbox("1개의 종을 선택하세요!!", iris.species.unique())
    st.write("선택된 species:", val)

    result = iris.loc[iris['species'] == val, :].reset_index(drop=True)
    st.data_editor(result)

    cols = st.multiselect("복수의 컬럼을 선택하세요!!", iris.columns)
    st.dataframe(iris.loc[:, cols])
    

if __name__ == "__main__":
    main()