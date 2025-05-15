import streamlit as st

st.set_page_config(page_title="도라에몽 캐릭터 심리 테스트", page_icon="🤖")

# 캐릭터 결과 매핑
characters = {
    "도라에몽": {
        "desc": "현실적이고 친구들을 잘 챙기는 해결사형! 도구도 많고 아이디어도 풍부해요.",
        "img": "https://upload.wikimedia.org/wikipedia/ko/thumb/7/72/Doraemon_character.png/240px-Doraemon_character.png"
    },
    "노진구": {
        "desc": "어딘가 부족하지만 정 많고 순수한 스타일! 운보다 우정을 믿는 당신은 진구!",
        "img": "https://i.namu.wiki/i/_Jg_xDvFjsmpSlLPhdEM8QHHkm0f1HfAarOTccS5Syy14TZJ7Uuq7m19H_1spIlBhTn3os7K_uC7OlwMjESVmg.webp"
    },
    "이슬이": {
        "desc": "현실적이고 똑 부러진 성격! 정리정돈 좋아하고 예의 바른 당신은 이슬이~",
        "img": "https://i.namu.wiki/i/2Rmpj6_UFRGz6TJgmRGdMiBt7nNm7DdJtL0PVXxH7F3Ru1O05RMrrqx3JJtGkBta_2J_HIlMSd0Aro7GejqJYw.webp"
    },
    "퉁퉁이": {
        "desc": "자기 주장이 강하고 리더쉽이 있어요! 가끔 욱하지만 따뜻한 마음의 소유자!",
        "img": "https://i.namu.wiki/i/DfYIko5D7QwCRcNKMZmdtIBaMQHQJAcPJ2zgeO1k_0IoFcQdbSFLV8S52GUaBL9AJhgNMWYxF5COAlDNlNgU1g.webp"
    },
    "비실이": {
        "desc": "감수성 풍부하고 섬세한 성격! 겉보기와 달리 마음 여리고 정 많아요~",
        "img": "https://i.namu.wiki/i/UP1_lU_NL-GBFoSt1Qfn6NKk9a2QnqOvFGEF9PLsh-BGvM5dVBcJ_BzgoOQPoLt3ArCJjwT4ivRYGibzmsuUew.webp"
    },
    "도라미": {
        "desc": "섬세하고 깔끔한 성격! 계획적인 걸 좋아하고 믿음직한 스타일이에요.",
        "img": "https://upload.wikimedia.org/wikipedia/ko/2/2a/Dorami.png"
    }
}

# 질문 목록 (점수 기반 분기)
questions = [
    {"question": "시험 전날 나는...", "A": ("일단 잔다", "진구"), "B": ("계획을 세운다", "도라미")},
    {"question": "친구가 울고 있어...", "A": ("같이 울어준다", "비실이"), "B": ("티슈를 챙겨준다", "도라에몽")},
    {"question": "소풍날 비가 온다면?", "A": ("운명이려니 한다", "진구"), "B": ("대안 계획을 바로 꺼낸다", "도라에몽")},
    {"question": "갈등이 생기면...", "A": ("먼저 사과한다", "이슬이"), "B": ("그냥 지나간다", "퉁퉁이")},
    {"question": "간식이 떨어졌다면?", "A": ("포기한다", "비실이"), "B": ("만들어 먹는다", "도라미")},
    {"question": "친구가 늦었을 때...", "A": ("기다려준다", "이슬이"), "B": ("화난 티 낸다", "퉁퉁이")},
    {"question": "새로운 걸 시작할 때...", "A": ("걱정부터 한다", "비실이"), "B": ("재밌겠는데?", "도라에몽")},
    {"question": "시험 끝난 날 나는...", "A": ("친구들이랑 놀러간다", "진구"), "B": ("혼자 집에서 쉰다", "도라미")}
]

# 초기 세션 상태 설정
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.scores = {k: 0 for k in characters}

# 질문 진행 중
if st.session_state.index < len(questions):
    q = questions[st.session_state.index]
    st.markdown(f"### Q{st.session_state.index + 1}. {q['question']}")
    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"👉 {q['A'][0]}", key="A"):
            st.session_state.scores[q['A'][1]] += 1
            st.session_state.index += 1
    with col2:
        if st.button(f"👉 {q['B'][0]}", key="B"):
            st.session_state.scores[q['B'][1]] += 1
            st.session_state.index += 1
    st.progress((st.session_state.index) / len(questions))
else:
    # 결과 계산
    result = max(st.session_state.scores, key=st.session_state.scores.get)
    st.markdown(f"## 당신은 **{result}** 스타일! 🎉")
    st.image(characters[result]["img"], width=250)
    st.markdown(f"📝 {characters[result]['desc']}")
    st.button("🔁 다시 시작하기", on_click=lambda: st.session_state.clear())
