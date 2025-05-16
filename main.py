import streamlit as st

st.set_page_config(page_title="도라에몽 캐릭터 심리 테스트", page_icon="🤖")

# 캐릭터 설명 및 이미지 (png로 확실하게 작동하는 링크 사용)
characters = {
    "도라에몽": {
        "desc": "문제를 해결해주는 든든한 해결사! 차분하고 배려심이 깊어요.",
        "img": "https://i.imgur.com/LzIuWfy.png"
    },
    "도라미": {
        "desc": "똑 부러지고 계획적인 완벽주의자! 실수 없는 스타일이에요.",
        "img": "https://i.imgur.com/PCzkdQJ.png"
    },
    "진구": {
        "desc": "조금은 덤벙대지만 마음만은 따뜻한 순수파!",
        "img": "https://i.imgur.com/9btP7fI.png"
    },
    "이슬이": {
        "desc": "예의 바르고 침착하며 지적인 성격의 소유자!",
        "img": "https://i.imgur.com/QOZZXKH.png"
    },
    "퉁퉁이": {
        "desc": "강한 리더십과 주도성! 가끔 욱하지만 책임감 있어요.",
        "img": "https://i.imgur.com/Khu31rK.png"
    },
    "비실이": {
        "desc": "감수성 풍부하고 표현력이 뛰어난 낭만파!",
        "img": "https://i.imgur.com/VhCIjOA.png"
    }
}

# 질문 정의
questions = [
    {"question": "시험 전날 나는...", 
     "A": ("일단 자고 본다", "진구"), 
     "B": ("계획표 짜고 공부한다", "이슬이")},
    {"question": "친구가 울고 있어!", 
     "A": ("같이 울어준다", "비실이"), 
     "B": ("티슈 주고 달래준다", "도라에몽")},
    {"question": "소풍날 비가 오면 나는...", 
     "A": ("그냥 운명인가보다", "진구"), 
     "B": ("대체 플랜을 실행한다!", "도라미")},
    {"question": "친구랑 싸우면 나는...", 
     "A": ("먼저 사과한다", "비실이"), 
     "B": ("그냥 시간 지나길 기다린다", "퉁퉁이")},
    {"question": "먹고 싶은 간식이 떨어졌다면?", 
     "A": ("포기한다", "진구"), 
     "B": ("직접 만들어 먹는다", "도라미")},
    {"question": "단체활동에서 나는...", 
     "A": ("리더를 맡는다", "퉁퉁이"), 
     "B": ("묵묵히 따라간다", "이슬이")},
    {"question": "시험 시간 5분 전, 나는?", 
     "A": ("멘붕", "진구"), 
     "B": ("마지막까지 훑는다", "도라미")}
]

# 초기 상태 설정
if "page" not in st.session_state:
    st.session_state.page = 0
if "scores" not in st.session_state:
    st.session_state.scores = {}

st.title("🧠 도라에몽 캐릭터 심리 테스트")
st.write("아래 질문에 답하며 당신의 성격과 닮은 도라에몽 캐릭터를 찾아보세요!")

# 진행 중
if st.session_state.page < len(questions):
    q = questions[st.session_state.page]
    st.markdown(f"**Q{st.session_state.page+1}. {q['question']}**")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🅰️ " + q["A"][0]):
            char = q["A"][1]
            st.session_state.scores[char] = st.session_state.scores.get(char, 0) + 1
            st.session_state.page += 1

    with col2:
        if st.button("🅱️ " + q["B"][0]):
            char = q["B"][1]
            st.session_state.scores[char] = st.session_state.scores.get(char, 0) + 1
            st.session_state.page += 1

    # 진행률 표시
    progress = (st.session_state.page) / len(questions)
    st.progress(progress)

# 결과 출력
else:
    st.subheader("✅ 결과 확인!")
    result = max(st.session_state.scores, key=st.session_state.scores.get)
    st.success(f"당신과 가장 닮은 캐릭터는 **{result}**!")

    st.image(characters[result]["img"], width=300)
    st.markdown(characters[result]["desc"])
    st.balloons()

    if st.button("🔁 다시하기"):
        st.session_state.page = 0
        st.session_state.scores = {}

