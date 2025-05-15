import streamlit as st

st.set_page_config(page_title="도라에몽 캐릭터 심리 테스트", page_icon="🤖")

# 캐릭터 정보 (설명 + 이미지) - 이미지 URL 공식 위키에서 가져온 안전한 것들로 교체
characters = {
    "도라에몽": {
        "desc": "현실적이고 친구들을 잘 챙기는 해결사형! 도구도 많고 아이디어도 풍부해요.",
        "img": "https://upload.wikimedia.org/wikipedia/ko/thumb/7/72/Doraemon_character.png/240px-Doraemon_character.png"
    },
    "노진구": {
        "desc": "어딘가 부족하지만 정 많고 순수한 스타일! 운보다 우정을 믿는 당신은 진구!",
        "img": "https://upload.wikimedia.org/wikipedia/ko/0/0a/Nobita_Nobi.svg"
    },
    "이슬이": {
        "desc": "현실적이고 똑 부러진 성격! 정리정돈 좋아하고 예의 바른 당신은 이슬이~",
        "img": "https://upload.wikimedia.org/wikipedia/ko/4/43/Shizuka_Minamoto.svg"
    },
    "퉁퉁이": {
        "desc": "자기 주장이 강하고 리더쉽이 있어요! 가끔 욱하지만 따뜻한 마음의 소유자!",
        "img": "https://upload.wikimedia.org/wikipedia/ko/8/81/Suneo_Honekawa.svg"
    },
    "비실이": {
        "desc": "감수성 풍부하고 섬세한 성격! 겉보기와 달리 마음 여리고 정 많아요~",
        "img": "https://upload.wikimedia.org/wikipedia/ko/1/1c/Doraemon_Bisilly.svg"
    },
    "도라미": {
        "desc": "섬세하고 깔끔한 성격! 계획적인 걸 좋아하고 믿음직한 스타일이에요.",
        "img": "https://upload.wikimedia.org/wikipedia/ko/2/2a/Dorami.png"
    }
}

# 질문 리스트
questions = [
    {"question": "시험 전날 나는...", "A": ("일단 잔다", "노진구"), "B": ("계획을 세운다", "도라미")},
    {"question": "친구가 울고 있어...", "A": ("같이 울어준다", "비실이"), "B": ("티슈를 챙겨준다", "도라에몽")},
    {"question": "소풍날 비가 온다면?", "A": ("운명이려니 한다", "노진구"), "B": ("대안 계획을 바로 꺼낸다", "도라에몽")},
    {"question": "갈등이 생기면...", "A": ("먼저 사과한다", "이슬이"), "B": ("그냥 지나간다", "퉁퉁이")},
    {"question": "간식이 떨어졌다면?", "A": ("포기한다", "비실이"), "B": ("직접 만들어 먹는다", "도라미")},
    {"question": "친구가 늦었을 때...", "A": ("기다려준다", "이슬이"), "B": ("화난 티 낸다", "퉁퉁이")},
    {"question": "새로운 걸 시작할 때...", "A": ("걱정부터 한다", "비실이"), "B": ("도전해본다", "도라에몽")},
    {"question": "여행가면 나는...", "A": ("계획 짜는 걸 좋아한다", "도라미"), "B": ("그냥 즉흥으로 즐긴다", "노진구")},
    {"question": "친구들과 모임에서 나는...", "A": ("주도적으로 이끈다", "퉁퉁이"), "B": ("조용히 듣고 맞장구 친다", "비실이")},
    {"question": "스트레스 받을 땐...", "A": ("운동하며 푼다", "도라에몽"), "B": ("혼자 조용히 시간을 보낸다", "이슬이")},
]

# 초기화
if "page" not in st.session_state:
    st.session_state.page = 0
if "scores" not in st.session_state:
    st.session_state.scores = {}

# 진행률 표시
st.progress(st.session_state.page / len(questions))

def show_question(idx):
    q = questions[idx]
    st.write(f"### Q{idx + 1}. {q['question']}")
    col1, col2 = st.columns(2)
    if col1.button(f"A. {q['A'][0]}"):
        char = q['A'][1]
        st.session_state.scores[char] = st.session_state.scores.get(char, 0) + 1
        st.session_state.page += 1
        st.experimental_rerun()
    if col2.button(f"B. {q['B'][0]}"):
        char = q['B'][1]
        st.session_state.scores[char] = st.session_state.scores.get(char, 0) + 1
        st.session_state.page += 1
        st.experimental_rerun()

def show_result():
    max_score = max(st.session_state.scores.values())
    winners = [k for k, v in st.session_state.scores.items() if v == max_score]
    result_char = winners[0]

    st.success(f"🎉 당신과 가장 닮은 도라에몽 캐릭터는 **{result_char}** 입니다!")
    st.write(characters[result_char]["desc"])
    st.image(characters[result_char]["img"], width=300)
    st.balloons()

if st.session_state.page < len(questions):
    show_question(st.session_state.page)
else:
    show_result()
