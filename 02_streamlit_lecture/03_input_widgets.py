"""
3단계: 입력 위젯
학습 목표: 사용자로부터 다양한 형태의 입력 받기
"""

import streamlit as st
from datetime import datetime, date, time

st.title("🎛️ 입력 위젯 배우기")

# ============================================
# 1. 텍스트 입력
# ============================================
st.header("1. 텍스트 입력")


st.subheader("한 줄 입력")
name = st.text_input(
    "이름을 입력하세요:",
    placeholder="유혜린",
    help="이름을 입력하는 필드입니다"
)
if name:
    st.write(f"입력한 이름: {name}")

email = st.text_input(
    "이메일:",
    placeholder="example@email.com",
    type="default"
)

password = st.text_input(
    "비밀번호:",
    type="password"
)

st.subheader("여러 줄 입력")
message = st.text_area(
    "메시지를 입력하세요:",
    placeholder="여기에 메시지를 작성하세요",
    height=200
)
if message:
    st.info(f"입력한 글자 수: {len(message)}자")

# ============================================
# 2. 숫자 입력
# ============================================
st.divider()
st.header("2. 숫자 입력")


st.subheader("숫자 직접 입력")
age = st.number_input(
    "나이:",
    min_value=0,
    max_value=120,
    value=33,
    step=1
)
st.write(f"입력한 나이: {age}세")

price = st.number_input(
    "가격:",
    min_value=0.0,
    value=10000.0,
    step=1000.0,
    format="%.2f"
)
st.write(f"₩{price:,.0f}")

st.subheader("슬라이더")
temperature = st.slider(
    "온도 (°C):",
    min_value=-10,
    max_value=40,
    value=20,
    step=1
)
st.write(f"현재 온도: {temperature}°C")

# 범위 슬라이더
price_range = st.slider(
    "가격 범위:",
    min_value=0,
    max_value=100000,
    value=(20000, 50000),
    step=5000,
    format="₩%d"
)
st.write(f"₩{price_range[0]:,} ~ ₩{price_range[1]:,}")

# ============================================
# 3. 선택 위젯
# ============================================
st.divider()
st.header("3. 선택 위젯")


st.subheader("드롭다운")
city = st.selectbox(
    "도시를 선택하세요:",
    ["서울", "부산", "대구", "인천", "광주", "대전", "울산"],
    index=0
)
st.write(f"선택한 도시: {city}")

st.subheader("라디오 버튼")
gender = st.radio(
    "성별:",
    ["남성", "여성", "기타"],
    horizontal=True
)
st.write(f"선택: {gender}")

st.subheader("다중 선택")
hobbies = st.multiselect(
    "취미를 선택하세요 (복수 선택 가능):",
    ["독서", "운동", "영화", "음악", "게임", "요리", "여행"],
    default=["독서", "운동"]
)
if hobbies:
    st.write(f"선택한 취미: {', '.join(hobbies)}")

st.subheader("선택형 슬라이더")
rating = st.select_slider(
    "만족도:",
    options=["매우 불만", "불만", "보통", "만족", "매우 만족"],
    value="보통"
)
st.write(f"평가: {rating}")

# ============================================
# 4. 체크박스와 토글
# ============================================
st.divider()
st.header("4. 체크박스와 토글")


agree = st.checkbox("이용약관에 동의합니다")
subscribe = st.checkbox("뉴스레터 구독", value=True)

if agree and subscribe:
    st.success("모두 동의하셨습니다!")

show_details = st.toggle("상세 정보 보기")

if show_details:
    st.info("📌 여기에 상세 정보가 표시됩니다.")

# ============================================
# 5. 버튼
# ============================================
st.divider()
st.header("5. 버튼")

if st.button("일반 버튼", use_container_width=True):
    st.write("버튼이 클릭되었습니다!")

if st.button("Primary 버튼", type="primary", use_container_width=True):
    st.balloons()

if st.button("🎨 아이콘 버튼", use_container_width=True):
    st.snow()

# ============================================
# 6. 날짜와 시간
# ============================================
st.divider()
st.header("6. 날짜와 시간")


selected_date = st.date_input(
    "날짜 선택:",
    value=date.today()
)
st.write(f"선택한 날짜: {selected_date}")

selected_time = st.time_input(
    "시간 선택:",
    value=time(9, 0)
)
st.write(f"선택한 시간: {selected_time}")

# ============================================
# 7. 파일 업로드
# ============================================
st.divider()
st.header("7. 파일 업로드")

uploaded_file = st.file_uploader(
    "파일을 선택하세요",
    type=['txt', 'csv', 'pdf', 'png', 'jpg'],
    help="txt, csv, pdf, png, jpg 파일만 업로드 가능합니다"
)

if uploaded_file is not None:
    st.success(f"✅ 파일 업로드 성공: {uploaded_file.name}")
    st.write(f"파일 크기: {uploaded_file.size} bytes")
    st.write(f"파일 타입: {uploaded_file.type}")
    
    # 이미지 파일인 경우 표시
    if uploaded_file.type.startswith('image'):
        st.image(uploaded_file, caption="업로드된 이미지")

# ============================================
# 실습 과제
# ============================================
st.divider()
st.header("📝 실습 과제")

st.markdown("""
### 과제 1: 회원가입 폼 만들기

다음 정보를 입력받는 회원가입 폼을 만들어보세요:
- 이름 (텍스트 입력)
- 이메일 (텍스트 입력, type="default")
- 비밀번호 (텍스트 입력, type="password")
- 생년월일 (날짜 선택)
- 성별 (라디오 버튼)
- 관심사 (다중 선택)
- 마케팅 수신 동의 (체크박스)
- 가입하기 버튼

버튼을 누르면 입력한 정보를 요약해서 보여주세요!

### 과제 2: BMI 계산기

- 키 입력 (숫자 또는 슬라이더, 단위: cm)
- 몸무게 입력 (숫자 또는 슬라이더, 단위: kg)
- 계산하기 버튼
- (BMI = 체중(kg) / (신장(m) * 신장(m)))
- BMI 결과 및 판정 표시
  - 저체중 (< 18.5)
  - 정상 (18.5 ~ 22.9)
  - 과체중 (23 ~ 24.9)
  - 비만 (≥ 25)
""")

import streamlit as st

st.title("BMI 계산기.💪")

st.markdown(
    """
    BMI(체질량지수)는 **체중(kg)** 을 **신장(m)의 제곱**으로 나눈 값입니다.  
    아래에서 키(cm)와 체중(kg)을 직접 입력한 뒤, 버튼을 눌러 BMI를 확인해 보세요.
    """
)

# 키 입력 (cm) - number_input
height_cm = st.number_input(
    "키 (cm)",
    min_value=100.0,
    max_value=250.0,
    value=170.0,
    step=0.5,
    format="%.1f"
)

# 체중 입력 (kg) - number_input
weight_kg = st.number_input(
    "체중 (kg)",
    min_value=20.0,
    max_value=200.0,
    value=65.0,
    step=0.5,
    format="%.1f"
)

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    if height_m <= 0:
        return None
    bmi = weight / (height_m ** 2)
    return round(bmi, 1)

# '측정하기' 버튼
if st.button("측정하기"):
    bmi = calculate_bmi(weight_kg, height_cm)

    if bmi is None:
        st.error("키 입력에 문제가 있습니다. 다시 확인해주세요.")
    else:
        st.subheader(f"당신의 BMI: **{bmi}**")

        # BMI 구간 분류
        if bmi < 18.5:
            status = "저체중"
            detail = "영양 상태와 식습관을 점검하고, 필요 시 전문가와 상담이 필요할 수 있습니다."
            color = "blue"
        elif 18.5 <= bmi <= 22.9:
            status = "정상 체중"
            detail = "현재 체중을 유지하기 위해 규칙적인 운동과 균형 잡힌 식단을 유지해 주세요."
            color = "green"
        elif 23 <= bmi <= 24.9:
            status = "과체중"
            detail = "가벼운 체중 조절과 생활습관 개선(식습관, 활동량 증가)을 고려해 볼 수 있습니다."
            color = "orange"
        else:  # bmi >= 25
            status = "비만"
            detail = "체중 관리가 필요할 수 있으며, 건강검진 및 전문가 상담을 권장합니다."
            color = "red"

        st.markdown(
            f"**판정: <span style='color:{color}'>{status}</span>**",
            unsafe_allow_html=True
        )
        st.write(detail)

        st.info(
            """
            ### BMI 구간(아시아/대한민국 기준)
            - 저체중: **BMI < 18.5**
            - 정상 체중: **18.5 ~ 22.9**
            - 과체중: **23.0 ~ 24.9**
            - 비만: **25.0 이상**
            """
        )
else:
    st.caption("키와 체중을 입력한 뒤, '측정하기' 버튼을 눌러주세요.")


# 예시 답안
with st.expander("💡 과제 1 예시 답안"):
    st.subheader("회원가입")
    
    with st.form("signup_form"):
        form_name = st.text_input("이름*")
        form_email = st.text_input("이메일*")
        form_password = st.text_input("비밀번호*", type="password")
        form_birth = st.date_input("생년월일*")
        form_gender = st.radio("성별*", ["남성", "여성", "기타"], horizontal=True)
        form_interests = st.multiselect(
            "관심사",
            ["스포츠", "음악", "영화", "독서", "게임", "요리"]
        )
        form_marketing = st.checkbox("마케팅 수신 동의")
        
        submitted = st.form_submit_button("가입하기", type="primary")
        
        if submitted:
            if form_name and form_email and form_password:
                st.success("✅ 회원가입이 완료되었습니다!")
                st.write("### 가입 정보")
                st.write(f"- 이름: {form_name}")
                st.write(f"- 이메일: {form_email}")
                st.write(f"- 생년월일: {form_birth}")
                st.write(f"- 성별: {form_gender}")
                st.write(f"- 관심사: {', '.join(form_interests) if form_interests else '없음'}")
                st.write(f"- 마케팅 수신: {'동의' if form_marketing else '미동의'}")
            else:
                st.error("❌ 필수 항목을 모두 입력해주세요!")

with st.expander("💡 과제 2 예시 답안"):
    st.subheader("BMI 계산기")
    
    bmi_height = st.number_input("키 (cm):", min_value=100.0, max_value=250.0, value=170.0, step=0.1)
    bmi_weight = st.number_input("몸무게 (kg):", min_value=30.0, max_value=200.0, value=65.0, step=0.1)
    
    if st.button("BMI 계산하기", type="primary"):
        # BMI = 체중(kg) / (신장(m) * 신장(m))
        height_m = bmi_height / 100
        bmi = bmi_weight / (height_m ** 2)
        
        st.metric("BMI", f"{bmi:.1f}")
        
        if bmi < 18.5:
            st.info("📊 판정: 저체중")
        elif bmi < 23:
            st.success("📊 판정: 정상")
        elif bmi < 25:
            st.warning("📊 판정: 과체중")
        else:
            st.error("📊 판정: 비만")
