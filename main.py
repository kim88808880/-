import streamlit as st

# 페이지 설정
st.set_page_config(page_title="트랄라렐로트랄라라 MBTI", page_icon="🎈")

# 질문 리스트
questions = [
    {"question": "파티에서 나는…", "A": ("사람들과 어울리는 게 좋아", "E"), "B": ("혼자 조용히 있는 게 좋아", "I")},
    {"question": "계획 세우는 걸 좋아해?", "A": ("물론이지!", "J"), "B": ("즉흥이 더 재밌지~", "P")},
    {"question": "친구가 고민을 털어놨어. 나는…", "A": ("논리적으로 해결책을 말해줌", "T"), "B": ("그냥 들어주고 공감함", "F")},
    {"question": "여행 전 나는…", "A": ("계획표를 만든다", "J"), "B": ("가서 정하지 뭐~", "P")},
    {"question": "팀플에서 나는…", "A": ("리더를 맡는다", "E"), "B": ("조용히 맡은 일만 한다", "I")},
    {"question": "정보를 처리할 때 나는…", "A": ("사실, 데이터 중심", "S"), "B": ("아이디어, 가능성 중심", "N")},
    {"question": "선물을 고를 때 나는…", "A": ("실용적인 걸 고른다", "T"), "B": ("상대 마음을 생각한다", "F")},
    {"question": "문제 해결 방식은?", "A": ("논리적 분석", "T"), "B": ("직감과 감정", "F")},
    {"question": "약속 시간은?", "A": ("꼭 지킨다", "J"), "B": ("대충 맞추면 되지", "P")},
    {"question": "어떤 환경이 더 편해?", "A": ("계획된 환경", "J"), "B": ("자유로운 환경", "P")}
]

# 세션 상태 초기화
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.answers = []

# 현재 질문 인덱스
q_index = st.session_state.current_q

# 진행 바 표시
st.progress((q_index) / len(questions))

# 질문 표시
if q_index < len(questions):
    q = questions[q_index]
    st.subheader(f"Q{q_index + 1}. {q['question']}")
    if st.button(q["A"][0]):
        st.session_state.answers.append(q["A"][1])
        st.session_state.current_q += 1
        st.experimental_rerun()
    if st.button(q["B"][0]):
        st.session_state.answers.append(q["B"][1])
        st.session_state.current_q += 1
        st.experimental_rerun()

# 결과 계산
else:
    st.subheader("🎉 테스트 결과")

    def get_mbti(answers):
        result = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
        for a in answers:
            result[a] += 1
        mbti = ""
        mbti += "E" if result["E"] >= result["I"] else "I"
        mbti += "S" if result["S"] >= result["N"] else "N"
        mbti += "T" if result["T"] >= result["F"] else "F"
        mbti += "J" if result["J"] >= result["P"] else "P"
        return mbti

    mbti_type = get_mbti(st.session_state.answers)
    st.success(f"당신의 트랄라렐로트랄라라 MBTI는 **{mbti_type}**입니다!")

    if st.button("다시 하기"):
        st.session_state.current_q = 0
        st.session_state.answers = []
        st.experimental_rerun()

