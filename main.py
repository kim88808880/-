pip install streamlit

import streamlit as st

st.set_page_config(page_title="트랄라렐로트랄라라 MBTI", page_icon="🧠")

# 질문 리스트
questions = [
    {
        "question": "1. 파티에서 나는…",
        "A": ("사람들과 어울리는 게 좋아", "E"),
        "B": ("조용히 구석에서 쉬는 게 좋아", "I")
    },
    {
        "question": "2. 계획 세우는 걸 좋아해?",
        "A": ("물론이지!", "J"),
        "B": ("즉흥이 더 재밌지~", "P")
    },
    {
        "question": "3. 친구가 고민을 털어놨어. 나는…",
        "A": ("논리적으로 해결책을 제시한다", "T"),
        "B": ("공감하고 위로해준다", "F")
    },
    {
        "question": "4. 여행 가기 전에 나는…",
        "A": ("철저히 계획 세운다", "J"),
        "B": ("그냥 가서 정한다", "P")
    },
    {
        "question": "5. 나는 새로운 아이디어가…",
        "A": ("신선하고 창의적이면 좋아", "N"),
        "B": ("현실적이고 실용적이면 좋아", "S")
    },
    # ... 나머지 질문도 이렇게 추가 (총 10개)
]

# 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = 0
    st.session_state.answers = []

# 질문 수
total_questions = len(questions)

def show_question():
    q = questions[st.session_state.page]
    st.write(f"### {q['question']}")
    if st.button(f"🅰️ {q['A'][0]}"):
        st.session_state.answers.append(q['A'][1])
        st.session_state.page += 1
    if st.button(f"🅱️ {q['B'][0]}"):
        st.session_state.answers.append(q['B'][1])
        st.session_state.page += 1

# 결과 계산
def calculate_result():
    from collections import Counter
    count = Counter(st.session_state.answers)
    result = ""
    result += "E" if count["E"] >= count["I"] else "I"
    result += "S" if count["S"] >= count["N"] else "N"
    result += "T" if count["T"] >= count["F"] else "F"
    result += "J" if count["J"] >= count["P"] else "P"
    return result

# 진행률 표시
progress = (st.session_state.page / total_questions)
st.progress(progress)

st.title("🎉 트랄라렐로트랄라라 MBTI 테스트")

if st.session_state.page < total_questions:
    show_question()
else:
    st.success("🎉 테스트 완료!")
    mbti = calculate_result()
    st.header(f"당신의 트랄라 MBTI는? 🧠 **{mbti}** 타입!")
    # 유형 설명도 추가 가능
    st.write("👉 이 유형은 모험을 즐기고 상상력이 풍부한 사람입니다. (예시 설명)")
    if st.button("🔁 다시하기"):
        st.session_state.page = 0
        st.session_state.answers = []
