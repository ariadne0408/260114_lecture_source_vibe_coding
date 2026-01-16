"""
1단계: Streamlit 소개 및 첫 번째 앱
학습 목표: Streamlit의 기본 구조 이해하기
"""

import streamlit as st

# 브라우저창 텝을 보면 아이콘과 페이지 타이틀이 바뀌어있는것을 볼 수 있다.
st.set_page_config(
    page_title="스트림릿과의 만남",
    page_icon="🎨",
    layout="wide"  # "centered" 또는 "wide"
)

# 제목 표시
st.title("🎉 나의 첫 Streamlit 앱")

# 간단한 텍스트 출력
st.write("안녕!! Streamlit에 오신 것을 환영해.")

# 구분선
st.divider()

# 자기소개 섹션
st.header("자기소개")
st.write("이름: 유혜린")
st.write("직업: 백조")
st.write("관심사: 데이터 시각화, 머신러닝")

# 구분선
st.divider()

# 간단한 인터랙션
st.subheader("버튼을 눌러보세요!")
if st.button("인사하기"):
    st.balloons()  # 풍선 애니메이션
    st.success("반갑습니다! 🎊")

#힐링타임
import streamlit as st
import time

st.set_page_config(page_title="귀여움 충전기", page_icon="🐾")

st.title("🐾 귀여움 충전기 🐾")
st.write("버튼을 눌러 귀여움을 충전해 보세요!")

# 애니메이션 / 완료 메시지를 표시할 자리
placeholder = st.empty()

# '귀여움 충전하기' 버튼
if st.button("귀여움 충전하기 💗"):
    # 1) 고양이, 강아지 애니메이션 GIF 표시
    with placeholder.container():
        st.image(
            "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
            caption="고양이 귀여움 충전 중...", use_column_width=True
        )
        st.image(
            "https://media.giphy.com/media/26BRIYgL96d3i5vKQ/giphy.gif",
            caption="강아지 귀여움 충전 중...", use_column_width=True
        )

    # 2) GIF가 재생되는 시간 동안 잠시 대기 (원하는 만큼 조절 가능)
    time.sleep(3)

    # 3) 애니메이션 대신 '충전 완료!' 텍스트 출력
    placeholder.markdown(
        "<h2 style='text-align: center;'>✨ 충전 완료! ✨</h2>",
        unsafe_allow_html=True
    )
    

# 정보 박스
st.info("💡 팁: 코드를 수정하고 저장하면 자동으로 새로고침됩니다!")

# ============================================
# 실습 과제
# ============================================
st.divider()
st.header("📝 실습 과제")
st.markdown("""
1. 제목을 자신의 이름으로 변경해보세요
2. 자기소개 내용을 본인의 정보로 바꿔보세요
3. 새로운 버튼을 추가하고, 클릭 시 다른 메시지가 나오도록 해보세요
4. `st.warning()` 또는 `st.error()` 함수를 사용해보세요
""")
