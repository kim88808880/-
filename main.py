import streamlit as st

st.set_page_config(page_title="트랄라렐로트랄라라 MBTI", page_icon="🧠")

# 질문 리스트
questions = [
    {"question": "파티에서 나는…", "A": ("사람들과 어울리는 게 좋아", "E"), "B": ("혼자 조용히 있는 게 좋아", "I")},
    {"question": "계획 세우는 걸 좋아해?", "A": ("물론이지!", "J"), "B": ("즉흥이 더 재밌지~", "P")},
    {"question": "친구가 고민을 털어놨어. 나는…", "A": ("논리적으로 해결책을 말해줌", "T"), "B": ("그냥 들어주고 공감함", "F")},
    {"question": "여행 전 나는…", "A": ("계획표를 만든다", "J"), "B": ("가서 정하지 뭐~", "P")},
    {"question": "팀플에서 나는…", "A": ("리더를 맡는다", "E"), "B": ("조용히 맡은 일만 한다", "I")},
    {"question": "정보를 처리할 때 나는…", "A": ("사실 위주로 본다", "S"), "B": ("아이디어 위주로 본다", "N")},
    {"question": "친구랑 갈등이 생기면?", "A": ("직접 말해서 해결", "T"), "B": ("분위기 보며 풀어본다", "F")},
    {"question": "주말엔 뭐해?", "A": ("계획대로 보낸다", "J"), "B": ("즉흥적으로 논다", "P")},
    {"question": "처음 보는 사람과 나는?", "A": ("말을 잘 건다", "E"), "B": ("조용히 있다", "I")},
    {"question": "결정할 때 나는?", "A": ("논리적으로 판단", "T"), "B": ("감정적으로 판단", "F")},
]

# 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = 0
if "answers" not in st.session_state:
    st.session_state.answers = []

# 질문 보여주기
def show_question(i):
    q = questions[i]
    st.write(f"**Q{i+1}. {q['question']}**")
    col1, col2 = st.columns(2)
    if col1.button("A. " + q["A"][0], key=f"a{i}"):
        st.session_state.answers.append(q["A"][1])
        st.session_state.page += 1
    if col2.button("B. " + q["B"][0], key=f"b{i}"):
        st.session_state.answers.append(q["B"][1])
        st.session_state.page += 1

# 결과 계산
def show_result():
    result = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    for ans in st.session_state.answers:
        result[ans] += 1
    mbti = ""
    mbti += "E" if result["E"] >= result["I"] else "I"
    mbti += "S" if result["S"] >= result["N"] else "N"
    mbti += "T" if result["T"] >= result["F"] else "F"
    mbti += "J" if result["J"] >= result["P"] else "P"
    
    st.success(f"당신의 트랄라렐로트랄라라 MBTI는: **{mbti}** 🎉")
    st.balloons()

# 진행률 표시
progress = st.session_state.page / len(questions)
st.progress(progress)

# 질문 또는 결과 출력
if st.session_state.page < len(questions):
    show_question(st.session_state.page)
else:
    show_result()
