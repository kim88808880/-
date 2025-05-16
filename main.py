import streamlit as st

st.set_page_config(page_title="도라에몽 캐릭터 심리 테스트", page_icon="🤖")

# 캐릭터 설명 및 이미지
characters = {
    "도라에몽": {
        "desc": "문제를 해결해주는 든든한 해결사! 차분하고 배려심이 깊어요.",
        "img": "https://i.imgur.com/H5IwBqX.png",
        "traits": {
            "성격 특징": "침착하고 이성적인 해결사. 도구를 활용해 문제를 해결하는 실용주의자",
            "장점 💡": "배려심 깊고 책임감 강함, 위기 대처 능력 뛰어남",
            "단점 ⚠️": "가끔 지나치게 현실적, 감성적인 면 부족",
            "잘 어울리는 친구 👯": "진구, 이슬이"
        }
    },
    "도라미": {
        "desc": "똑 부러지고 계획적인 완벽주의자!",
        "img": "https://i.imgur.com/9qgoEo5.png",
        "traits": {
            "성격 특징": "계획적이고 완벽주의자. 깔끔한 걸 좋아하고 실수를 싫어함",
            "장점 💡": "체계적이고 신중함, 효율적인 일 처리",
            "단점 ⚠️": "융통성 부족, 실수에 예민함",
            "잘 어울리는 친구 👯": "이슬이, 도라에몽"
        }
    },
    "진구": {
        "desc": "조금은 덤벙대지만 마음만은 따뜻한 순수파!",
        "img": "https://i.imgur.com/vgUcoTr.png",
        "traits": {
            "성격 특징": "게으르지만 따뜻한 감성파. 순수하고 정 많음",
            "장점 💡": "감정이입 잘함, 창의적 상상력, 의외의 기지",
            "단점 ⚠️": "우유부단, 실행력 부족, 귀찮음 많음",
            "잘 어울리는 친구 👯": "도라에몽, 비실이"
        }
    },
    "이슬이": {
        "desc": "예의 바르고 침착하며 지적인 성격의 소유자!",
        "img": "https://i.imgur.com/L8ZH5hf.png",
        "traits": {
            "성격 특징": "차분하고 지적인 공감형. 감정 조절 잘함",
            "장점 💡": "예의 있고 학업 성실, 공감 능력 뛰어남",
            "단점 ⚠️": "자기 감정 숨김, 지나치게 착함",
            "잘 어울리는 친구 👯": "도라미, 도라에몽"
        }
    },
    "퉁퉁이": {
        "desc": "자기주장이 강하고 리더십 있는 열정파!",
        "img": "https://i.imgur.com/zxXMeRM.png",
        "traits": {
            "성격 특징": "강한 추진력과 자신감, 감정 표현이 직설적",
            "장점 💡": "리더십 있음, 추진력 좋음",
            "단점 ⚠️": "과격한 면, 고집 셈",
            "잘 어울리는 친구 👯": "비실이, 진구"
        }
    },
    "비실이": {
        "desc": "감수성 풍부하고 섬세한 스타일! 눈물도 많고 정 많아요.",
        "img": "https://i.imgur.com/M6GcYKR.png",
        "traits": {
            "성격 특징": "감정에 민감한 감성파. 소심하지만 따뜻함",
            "장점 💡": "예민하고 섬세함, 감정 공감 잘함",
            "단점 ⚠️": "겁 많고 자기 주장 약함",
            "잘 어울리는 친구 👯": "진구, 이슬이"
        }
    }
}

# 질문 리스트
questions = [
    {"question": "시험 전날 나는...", "A": ("일단 자고 본다", "진구"), "B": ("계획표 짜고 공부한다", "이슬이")},
    {"question": "친구가 울고 있어!", "A": ("같이 울어준다", "비실이"), "B": ("티슈 주고 달래준다", "도라에몽")},
    {"question": "소풍날 비가 오면 나는...", "A": ("그냥 운명인가보다", "진구"), "B": ("대체 플랜 실행!", "도라미")},
    {"question": "친구랑 싸우면 나는...", "A": ("먼저 사과한다", "비실이"), "B": ("그냥 시간 지나길 기다린다", "퉁퉁이")},
    {"question": "먹고 싶은 간식이 떨어졌다면?", "A": ("포기한다", "진구"), "B": ("직접 만들어 먹는다", "도라미")},
    {"question": "단체활동에서 나는...", "A": ("리더를 맡는다", "퉁퉁이"), "B": ("묵묵히 따라간다", "이슬이")},
    {"question": "시험 시간 5분 전, 나는?", "A": ("멘붕", "진구"), "B": ("마지막까지 훑는다", "도라미")}
]

# 초기 세션 상태
if "page" not in st.session_state:
    st.session_state.page = 0
if "scores" not in st.session_state:
    st.session_state.scores = {char: 0 for char in characters}

# 질문 진행
if st.session_state.page < len(questions):
    q = questions[st.session_state.page]
    st.progress((st.session_state.page) / len(questions))
    st.subheader(f"Q{st.session_state.page + 1}. {q['question']}")

    if st.button(f"A. {q['A'][0]}"):
        st.session_state.scores[q['A'][1]] += 1
        st.session_state.page += 1
    if st.button(f"B. {q['B'][0]}"):
        st.session_state.scores[q['B'][1]] += 1
        st.session_state.page += 1

# 결과 출력
else:
    st.success("🎉 테스트 완료! 당신과 닮은 도라에몽 캐릭터는...")
    result = max(st.session_state.scores, key=st.session_state.scores.get)
    char_info = characters[result]

    st.header(f"👉 {result} 타입")
    st.image(char_info["img"], width=300)
    st.markdown(f"**{char_info['desc']}**")

    st.markdown("### 📋 성격 분석")
    for key, value in char_info["traits"].items():
        st.markdown(f"**{key}**: {value}")

    st.button("🔄 다시 하기", on_click=lambda: [st.session_state.clear()])


