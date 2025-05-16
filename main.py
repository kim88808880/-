import streamlit as st

st.set_page_config(page_title="도라에몽 캐릭터 심리 테스트", page_icon="🤖")

# 캐릭터 설명 및 이미지
characters = {
    "도라에몽": {
        "desc": "문제를 해결해주는 든든한 해결사! 차분하고 배려심이 깊어요.",
        "img": "https://i.imgur.com/H5IwBqX.png"
    },
    "도라미": {
        "desc": "똑 부러지고 계획적인 완벽주의자! 실수 없는 스타일이에요.",
        "img": "https://i.imgur.com/9qgoEo5.png"
    },
    "진구": {
        "desc": "조금은 덤벙대지만 마음만은 따뜻한 순수파!",
        "img": "https://i.imgur.com/vgUcoTr.png"
    },
    "이슬이": {
        "desc": "예의 바르고 침착하며 지적인 성격의 소유자!",
        "img": "https://i.imgur.com/L8ZH5hf.png"
    },
    "퉁퉁이": {
        "desc": "자기주장이 강하고 리더십 있는 열정파!",
        "img": "https://i.imgur.com/zxXMeRM.png"
    },
    "비실이": {
        "desc": "감수성 풍부하고 섬세한 스타일! 눈물도 많고 정 많아요.",
        "img": "https://i.imgur.com/LzMLksr.png"
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

# 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = 0
if "scores" not in st.session_state:
    st.session_state.scores = {name: 0 for name in characters}

# 질문 진행
if st.session_state.page < len(questions):
    q = questions[st.session_state.page]
    st.markdown(f"### Q{st.session_state.page + 1}. {q['question']}")

    # 진행률 표시
    st.progress((st.session_state.page) / len(questions))

    col1, col2 = st.columns(2)
    with col1:
        if st.button(q["A"][0], key="A"):
            st.session_state.scores[q["A"][1]] += 1
            st.session_state.page += 1
    with col2:
        if st.button(q["B"][0], key="B"):
            st.session_state.scores[q["B"][1]] += 1
            st.session_state.page += 1

# 결과 출력
else:
    st.markdown("## 당신의 도라에몽 캐릭터는...")
    result = max(st.session_state.scores, key=st.session_state.scores.get)
    st.markdown(f"### 🧠 {result}")
    st.image(characters[result]["img"], width=200)
    st.write(characters[result]["desc"])

    # 다시 시작
    if st.button("🔁 다시 테스트하기"):
        st.session_state.page = 0
        st.session_state.scores = {name: 0 for name in characters}


