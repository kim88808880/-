import streamlit as st

st.set_page_config(page_title="트랄라렐로트랄라라 MBTI", page_icon="🧠")

# 질문 데이터
questions = [
    {"question": "파티에서 나는…", "A": ("사람들과 어울리는 게 좋아", "E"), "B": ("혼자 조용히 있는 게 좋아", "I")},
    {"question": "계획 세우는 걸 좋아해?", "A": ("물론이지!", "J"), "B": ("즉흥이 더 재밌지~", "P")},
    {"question": "친구가 고민을 털어놨어. 나는…", "A": ("논리적으로 해결책을 말해줌", "T"), "B": ("그냥 들어주고 공감함", "F")},
    {"question": "여행 전 나는…", "A": ("계획표를 만든다", "J"), "B": ("가서 정하지 뭐~", "P")},
    {"question": "팀플에서 나는…", "A": ("리더를 맡는다", "E"), "B": ("조용히 맡은 일만 한다", "I")},
    {"question": "정보를 처리할 때 나는…", "A": ("사실과 데이터 중심", "S"), "B": ("직감과 영감 중심", "N")},
    {"question": "문제 해결 방식은?", "A": ("객관적인 분석", "T"), "B": ("사람 중심으로 접근", "F")},
    {"question": "나는 더 편한 건?", "A": ("정돈된 일정", "J"), "B": ("유연한 일정", "P")},
    {"question": "아이디어 회의할 때 나는…", "A": ("현실적인 제안을 함", "S"), "B": ("창의적인 상상을 함", "N")},
    {"question": "사람을 만났을 때 나는…", "A": ("먼저 말을 건다", "E"), "B": ("상대가 먼저 말하면 반응", "I")},
]

# 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = 0
    st.session_state.answers = []

# 현재 페이지가 질문 단계라면
if st.session_state.page < len(questions):
    q = questions[st.session_state.page]
    st.markdown(f"### Q{st.session_state.page + 1}. {q['question']}")
    st.progress((st.session_state.page + 1) / len(questions))

    # 선택 버튼
    if st.button(q["A"][0]):
        st.session_state.answers.append(q["A"][1])
        st.session_state.page += 1
        st.experimental_rerun()

    if st.button(q["B"][0]):
        st.session_state.answers.append(q["B"][1])
        st.session_state.page += 1
        st.experimental_rerun()

# 결과 페이지
else:
    st.markdown("## 🎉 당신의 트랄라렐로트랄라라 MBTI는?")
    # 카운트 세기
    type_counts = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    for t in st.session_state.answers:
        type_counts[t] += 1

    # 최종 MBTI 계산
    mbti = ""
    mbti += "E" if type_counts["E"] >= type_counts["I"] else "I"
    mbti += "S" if type_counts["S"] >= type_counts["N"] else "N"
    mbti += "T" if type_counts["T"] >= type_counts["F"] else "F"
    mbti += "J" if type_counts["J"] >= type_counts["P"] else "P"

    st.success(f"당신의 유형은 **{mbti}** 입니다!")
    st.markdown("👉 친구에게 공유해보세요!")

    st.button("처음부터 다시 하기", on_click=lambda: st.session_state.clear())
