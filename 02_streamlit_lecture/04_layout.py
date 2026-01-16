"""
4단계: 레이아웃과 컨테이너
학습 목표: 페이지 구조를 체계적으로 구성하기
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="레이아웃 배우기",
    page_icon="🎨",
    layout="wide"  # "centered" 또는 "wide"
)

st.title("🎨 레이아웃 구성하기")

# ============================================
# 1. 사이드바
# ============================================
st.sidebar.title("⚙️ 설정 패널")
st.sidebar.write("사이드바는 설정이나 필터를 배치하기 좋습니다.")

sidebar_option = st.sidebar.selectbox(
    "옵션 선택:",
    ["옵션 1", "옵션 2", "옵션 3"]
)

sidebar_slider = st.sidebar.slider(
    "값 조정:",
    0, 100, 50
)

st.sidebar.divider()
st.sidebar.info(f"""
**현재 설정**
- 선택: {sidebar_option}
- 값: {sidebar_slider}
""")

# ============================================
# 2. 컬럼 레이아웃
# ============================================
st.header("1. 컬럼 레이아웃")

st.subheader("3개 컬럼 (1:1:1 비율)")
col1, col2, col3 = st.columns([1, 1.5, 1])

with col1:
    st.write("**왼쪽 컬럼**")
    st.button("두바이", use_container_width=True)

with col2:
    st.write("**가운데 컬럼**")
    st.button("쫀득", use_container_width=True)

with col3:
    st.write("**오른쪽 컬럼**")
    st.button("쿠키", use_container_width=True)    


# 구분선
st.divider()

st.subheader("3개 컬럼 (1:2:1 비율)")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.metric("사용자", "1,234", "+12%")

with col2:
    st.write("중앙 컬럼은 넓게!")
    st.progress(0.7)

with col3:
    st.metric("매출", "₩5M", "+8%")

# ============================================
# 3. 탭
# ============================================
st.divider()
st.header("2. 탭 레이아웃")

tab1, tab2, tab3  = st.tabs(["⚙️ 설정", "ℹ️ 정보", "바보"])

with tab1:
    st.subheader("설정 탭")
    
    theme = st.selectbox("테마:", ["라이트", "다크"])
    language = st.selectbox("언어:", ["한국어", "English"])
    
    if st.button("설정 저장"):
        st.success("설정이 저장되었습니다!")

with tab2:
    st.subheader("정보 탭")
    st.info("""
    **버전**: 1.0.0  
    **개발자**: Streamlit Team  
    **라이선스**: MIT
    """)

with tab3:
    st.subheader("바보 탭")
    st.info("""
    **버전**: 1.0.0  
    **개발자**: Streamlit Team  
    **라이선스**: MIT
    """)    

# ============================================
# 4. 확장 가능한 섹션 (Expander)
# ============================================
st.divider()
st.header("3. 확장 섹션 (Expander)")

with st.expander("📖 더 자세히 보기"):
    st.write("""
    여기는 기본적으로 숨겨져 있는 내용입니다.
    클릭하면 펼쳐집니다!
    """)
    st.code("""
    def hello():
        return "Hello, World!"
    """, language="python")

with st.expander("📊 통계 데이터", expanded=True):
    st.write("expanded=True로 설정하면 기본으로 펼쳐져 있습니다.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("방문자", "1,234")
    col2.metric("페이지뷰", "5,678")
    col3.metric("전환율", "3.2%")

# ============================================
# 5. Empty (동적 업데이트)
# ============================================
st.divider()
st.header("5. Empty (동적 업데이트)")

import time

placeholder = st.empty()

if st.button("카운트다운 시작"):
    for i in range(5, 0, -1):
        placeholder.write(f"⏰ {i}초 남았습니다...")
        time.sleep(1) # 1초 기다리기
    placeholder.success("✅ 완료!")

# ============================================
# 실습 과제
# ============================================
st.divider()
st.header("📝 실습 과제")

st.markdown("""
### 과제 1: 제품 상세 페이지 만들기

다음 레이아웃으로 제품 상세 페이지를 만드세요:

**구조:**
1. 사이드바: 카테고리 선택, 가격 범위 필터
2. 메인 영역:
   - 2개 컬럼 (1:1): 왼쪽에 이미지, 오른쪽에 상품 정보
   - 탭: 상세설명, 리뷰, 배송정보
   - Expander: FAQ
""")

import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="제품 상세 페이지",
    page_icon="🛒",
    layout="wide"
)

# ---------------------------
# 예시 데이터
# ---------------------------
categories = ["전체", "전자제품", "패션", "생활용품", "식품"]

product = {
    "name": "프리미엄 무선 헤드폰",
    "brand": "AI SOUND",
    "category": "전자제품",
    "price": 129000,
    "sale_price": 99000,
    "rating": 4.6,
    "review_count": 182,
    "stock": 42,
    "shipping": "무료배송",
    "delivery": "오늘 출발 (평일 오후 3시 전 주문 시)",
    "image_url": "https://images.pexels.com/photos/3394664/pexels-photo-3394664.jpeg",
    "summary": "노이즈 캔슬링, 최대 30시간 사용 가능한 프리미엄 무선 헤드폰",
    "detail_text": """
### 프리미엄 사운드 & 노이즈 캔슬링
- 액티브 노이즈 캔슬링(ANC)으로 소음 차단  
- 최대 30시간 사용 가능한 배터리  
- 블루투스 5.3, 자동 페어링 지원  

### 편안한 착용감
- 인체공학적 설계의 이어컵  
- 장시간 착용에도 부담을 줄인 무게 밸런스  

### 간편한 휴대성
- 접이식 디자인으로 보관 및 이동이 용이  
- 동봉된 파우치로 안전하게 보관 가능  
""",
    "shipping_info": """
- 배송방법: 택배  
- 배송비: 무료 (도서산간/제주 추가 요금 없음)  
- 출고지: 서울 물류센터  
- 평일 오후 3시 이전 결제 시 당일 출고  
- 평균 배송기간: 1~2일 (지역에 따라 상이)
"""
}

reviews = [
    {"user": "user01", "rating": 5, "content": "노이즈 캔슬링이 너무 좋아요. 지하철에서 효과 확실합니다.", "date": "2025-01-05"},
    {"user": "soundlover", "rating": 4, "content": "음질 좋고 배터리 오래가요. 다만 케이스가 조금 큰 편입니다.", "date": "2025-01-03"},
    {"user": "minsu", "rating": 5, "content": "가성비 최고입니다. 재구매 의사 있어요.", "date": "2025-01-01"}
]

faq_list = [
    {
        "q": "Q. 블루투스 미지원 기기에도 사용할 수 있나요?",
        "a": "A. 동봉된 3.5mm 오디오 케이블을 사용하면 유선으로도 사용 가능합니다."
    },
    {
        "q": "Q. 완충까지 충전 시간은 얼마나 걸리나요?",
        "a": "A. 완전 방전 상태 기준 약 2시간 정도 소요됩니다."
    },
    {
        "q": "Q. 방수 기능이 있나요?",
        "a": "A. 생활 방수 수준(IPX4)으로 땀이나 가벼운 빗방울은 견디지만, 물에 담그는 사용은 피해주세요."
    },
]

# ---------------------------
# 사이드바: 카테고리 & 가격 범위 필터
# ---------------------------
with st.sidebar:
    st.header("필터")

    selected_category = st.selectbox("카테고리 선택", categories)

    price_min, price_max = st.slider(
        "가격 범위 (원)",
        min_value=0,
        max_value=300000,
        value=(50000, 200000),
        step=10000,
        format="%d원"
    )

    st.caption(
        f"선택된 가격 범위: {price_min:,}원 ~ {price_max:,}원"
    )

    # 간단한 필터 결과 표시
    show_product = True
    if selected_category != "전체" and product["category"] != selected_category:
        show_product = False
    if not (price_min <= product["sale_price"] <= price_max):
        show_product = False

# ---------------------------
# 메인 영역
# ---------------------------
st.title("제품 상세 페이지")

if not show_product:
    st.warning("현재 필터 조건에 맞는 상품이 없습니다. 필터를 조정해 보세요.")
    st.stop()

# 2개 컬럼 (1:1) - 왼쪽 이미지, 오른쪽 상품 정보
left_col, right_col = st.columns(2)

with left_col:
    # use_column_width 제거, 대신 width 사용 (예: 500px)
    st.image(product["image_url"], width=500)
    st.caption(f"{product['brand']} | {product['name']}")

with right_col:
    st.subheader(product["name"])
    st.text(product["summary"])

    # 가격 정보
    st.markdown("---")
    st.markdown(
        f"""
        <div style="font-size:14px; color:gray;">
            정상가 <s>{product['price']:,}원</s>
        </div>
        <div style="font-size:26px; font-weight:700; color:#ff4b4b;">
            {product['sale_price']:,}원
        </div>
        """,
        unsafe_allow_html=True
    )

    # 평점, 리뷰, 재고
    st.write(
        f"⭐ **{product['rating']} / 5.0**  |  리뷰 {product['review_count']}개  |  재고 {product['stock']}개 남음"
    )

    # 배송/출고 정보
    st.markdown("---")
    st.write(f"**배송비:** {product['shipping']}")
    st.write(f"**출고 안내:** {product['delivery']}")

    # 옵션/수량
    color = st.selectbox("색상 선택", ["블랙", "화이트", "블루"])
    quantity = st.number_input("수량", min_value=1, max_value=10, value=1, step=1)

    total_price = product["sale_price"] * quantity
    st.markdown(
        f"**총 상품 금액:** :red[{total_price:,}원]"
    )

    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        buy_now = st.button("✅ 바로 구매하기", use_container_width=True)
    with col_btn2:
        add_cart = st.button("🛒 장바구니 담기", use_container_width=True)

    if buy_now:
        st.success(
            f"'{product['name']}' ({color}, {quantity}개)를 구매하기로 선택하셨습니다."
        )
    if add_cart:
        st.info(
            f"장바구니에 '{product['name']}' ({color}, {quantity}개)가 담겼습니다."
        )

st.markdown("---")

# ---------------------------
# 탭: 상세설명, 리뷰, 배송정보
# ---------------------------
tab1, tab2, tab3 = st.tabs(["상세설명", "리뷰", "배송정보"])

with tab1:
    st.subheader("상품 상세설명")
    st.markdown(product["detail_text"])

with tab2:
    st.subheader("상품 리뷰")
    if not reviews:
        st.write("등록된 리뷰가 없습니다.")
    else:
        for r in reviews:
            st.markdown(f"**{r['user']}**  |  ⭐ {r['rating']}  |  {r['date']}")
            st.write(r["content"])
            st.markdown("---")

    # 리뷰 작성 폼 (예시)
    st.write("### 리뷰 작성하기")
    new_rating = st.slider("평점", 1, 5, 5)
    new_content = st.text_area("리뷰 내용", placeholder="제품 사용 경험을 남겨주세요.")
    if st.button("리뷰 등록"):
        if new_content.strip() == "":
            st.error("리뷰 내용을 입력해주세요.")
        else:
            st.success("리뷰가 등록되었습니다. (데모라 실제 저장은 되지 않습니다.)")

with tab3:
    st.subheader("배송정보")
    st.markdown(product["shipping_info"])

# ---------------------------
# Expander: FAQ
# ---------------------------
with st.expander("❓ 자주 묻는 질문(FAQ)", expanded=False):
    for item in faq_list:
        st.markdown(f"**{item['q']}**")
        st.write(item["a"])
        st.markdown("---")


# 예시 답안
with st.expander("💡 과제 1 예시 답안"):
    st.subheader("제품 상세 페이지")
    
    # 2컬럼 레이아웃
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ96jQ9W4bT93OXaPYPMiX3hSW3ioFRp-2mCA&s", use_container_width=True)
    
    with col2:
        st.write("### 🎧 무선 헤드폰 Pro")
        st.write("**₩299,000**")
        st.write("⭐⭐⭐⭐⭐ (4.8) - 리뷰 324개")
        st.write("---")
        st.write("고급 노이즈 캔슬링 기능이 탑재된 프리미엄 무선 헤드폰")
        
        quantity = st.number_input("수량:", min_value=1, value=1)
        col_a, col_b = st.columns(2)
        col_a.button("🛒 장바구니", use_container_width=True)
        col_b.button("💳 바로 구매", type="primary", use_container_width=True)
    
    # 탭
    tab1, tab2, tab3 = st.tabs(["📋 상세설명", "⭐ 리뷰", "🚚 배송정보"])
    
    with tab1:
        st.write("**주요 특징**")
        st.write("- 최대 30시간 재생")
        st.write("- 고급 노이즈 캔슬링")
        st.write("- 블루투스 5.0")
    
    with tab2:
        st.write("평균 평점: ⭐ 4.8/5.0")
        st.write("---")
        st.write("**김철수**: ⭐⭐⭐⭐⭐")
        st.write("정말 좋아요!")
    
    with tab3:
        st.info("무료 배송 (2-3일 소요)")
    
    # FAQ
    with st.expander("❓ 자주 묻는 질문"):
        st.write("**Q: 배송은 얼마나 걸리나요?**")
        st.write("A: 보통 2-3일 소요됩니다.")

with st.expander("💡 과제 2 예시 답안"):
    st.subheader("데이터 분석 대시보드")
    
    # 상단 메트릭
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("총 방문자", "12,345", "+8%")
    m2.metric("페이지뷰", "45,678", "+12%")
    m3.metric("전환율", "3.2%", "-0.3%")
    m4.metric("평균 체류", "5:23", "+15s")
    
    # 중단
    left, right = st.columns([2, 1])
    
    with left:
        st.write("**방문자 추이**")
        data = pd.DataFrame(
            np.random.randint(100, 200, 30),
            columns=['방문자']
        )
        st.line_chart(data)
    
    with right:
        st.write("**필터**")
        period = st.selectbox("기간:", ["오늘", "7일", "30일", "90일"])
        source = st.multiselect("소스:", ["검색", "SNS", "직접", "광고"])
        st.button("적용", type="primary", use_container_width=True)
    
    # 하단 탭
    t1, t2, t3 = st.tabs(["📊 데이터", "📈 통계", "⚙️ 설정"])
    
    with t1:
        sample_df = pd.DataFrame({
            '날짜': pd.date_range('2026-01-01', periods=5),
            '방문자': [120, 145, 132, 156, 143]
        })
        st.dataframe(sample_df, use_container_width=True)
    
    with t2:
        st.write("평균 방문자:", data['방문자'].mean())
        st.write("최대값:", data['방문자'].max())
        st.write("최소값:", data['방문자'].min())
    
    with t3:
        st.write("대시보드 설정")
        st.checkbox("자동 새로고침")
        st.selectbox("새로고침 간격:", ["1분", "5분", "10분"])
