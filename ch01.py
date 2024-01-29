import streamlit as st
import streamlit.components.v1 as components

def main():
    
    st.markdown("HTML JS Streamlit 적용")
    js_code = """ 
    <h3>Hi</h3>
    <script>
    function sayHello() {
        alert('Hello from JavaScript in Streamlit Web');
    }
    </script>
    <button onclick="sayHello()">Click me</button>
    """
    components.html(js_code) # 위의 것은 자바스크립트 적용 예시.



    st.title("안녕하세요!!")
    st.header("This is Header")
    st.subheader("이것은 서브헤더입니다.")
    st.write("파이썬 문법 사용 가능")
    st.write("-" * 50) # 프린트 함수와 유사함(-를 50개 넣어서 <hr>(중간줄)과 같은 효과를 냈다.)
    a = 1
    b = 2
    st.write(a + b)
    st.write("+" * 10 + "-" * 10)
    st.markdown("$\.{a}$") # 라텍스 코드 적용 된다! 따옴표 안에 달러표시가 필요함!
    st.markdown("""
                $\begin{pmatrix}
                 a & b\\
                 c & d
                \end{pmatrix}$
                """) # 이건 달러가 들어가도 안되는데....
    
    st.latex(r'''
            \begin{pmatrix}
             a & b\\
             c & d
            \end{pmatrix}
            ''') # 이렇게 하니까 메트릭스가 표현이 되는구나. 메소드를 markdown이 아니라, latex를 이용해야 함.
    

    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
    st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

    multi = '''If you end a line with two spaces,
    a soft return is used for the next line.

    Two (or more) newline characters in a row will result in a hard return.
    '''
    st.markdown(multi)

    st.markdown("""
                ## Chapter.1 수식
                - 피타고라스 정리 : :red[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:
                """) # 달러 표시는 라텍스 문법을 썼다는 의미라 함.
    
    st.markdown("## Chapter 2. \n"
                "- Streamlit is **_really_ cool**.\n"
                "   * This text is :blue[colored blue], and this is **:red[colored] ** and bold.") # 개행 사이에 보면 쉼표가 없는 것이 특징.
    
    # 이하 코드에 대한 내용. html css도 불러올 수 있음을 보여주는 코드임.
    # 1. 외부에서 style.css 파일 불러오고 string으로 변환
    # 2. string으로 변환한 것으로 기존 HTML code와 접목
    # "<style>" + style + </style> + HTML
    # 해당 내용을 아래의 코드와 비교해볼 것.

    st.markdown("HTML CSS 마크다운 적용")
    html_css = """
    <style>
        table.customTable {
        width: 100%;
        background-color: #FFFFFF;
        border-collapse: collapse;
        border-width: 2px;
        border-color: #7ea8f8;
        border-style: solid;
        color: #000000;
        }
    </style>
    <table class="customTable">
      <thead>
        <tr>
          <th>이름</th>
          <th>나이</th>
          <th>직업</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Evan</td>
          <td>25</td>
          <td>데이터 분석가</td>
        </tr>
        <tr>
          <td>Sara</td>
          <td>25</td>
          <td>프로덕트 오너</td>
        </tr>
      </tbody>
    </table>
    """
    st.markdown(html_css, unsafe_allow_html=True) # unsafe_allow_html=True가 항상 있어야 한다 함.

if __name__ == "__main__":
    main() # 이름이 메인이면 메인함수를 실행