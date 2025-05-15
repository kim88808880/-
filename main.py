import streamlit as st

st.set_page_config(page_title="도라에몽 캐릭터 심리 테스트", page_icon="🤖")

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

# 현재 질문
if st.session_state.page < len(questions):
    q = questions[st.session_state.page]
    
    st.markdown(f"### Q{st.session_state.page + 1}. {q['question']}")
    
    # 선택 버튼
    if st.button("🅰️ " + q["A"][0]):
        char = q["A"][1]
        st.session_state.scores[char] = st.session_state.scores.get(char, 0) + 1
        st.session_state.page += 1

    if st.button("🅱️ " + q["B"][0]):
        char = q["B"][1]
        st.session_state.scores[char] = st.session_state.scores.get(char, 0) + 1
        st.session_state.page += 1

    # 진도 표시
    progress = (st.session_state.page / len(questions))
    st.progress(progress)

else:
    # 결과 계산
    result = max(st.session_state.scores, key=st.session_state.scores.get)

    st.markdown("## 🎉 당신과 가장 닮은 도라에몽 캐릭터는?")
    
    character_profiles = {
        "도라에몽": "🤖 현실적이고 도움을 잘 주는 만능 해결사!",
        "진구": "😅 덜렁대지만 순수하고 정 많은 친구~",
        "이슬이": "🎓 똑똑하고 책임감 있는 엘리트!",
        "퉁퉁이": "💪 강한 리더십과 자신감의 소유자!",
        "비실이": "🎤 감수성 풍부한 예술가 스타일!",
        "도라미": "🧼 꼼꼼하고 계획적인 완벽주의자!"
    }

    st.subheader(result)
    st.write(character_profiles[result])

    st.button("🔄 다시 하기", on_click=lambda: st.session_state.clear())
