import streamlit as st
import pandas as pd

st.set_page_config(page_title="도라에몽 캐릭터 심리 테스트", page_icon="🤖")

# 캐릭터 데이터
characters = {
    "도라에몽": {
        "desc": "문제를 해결해주는 든든한 해결사! 차분하고 배려심이 깊어요.",
        "img": "https://www.google.co.kr/url?sa=i&url=https%3A%2F%2Fko.wikipedia.org%2Fwiki%2F%25EB%258F%2584%25EB%259D%25BC%25EC%2597%2590%25EB%25AA%25BD_%2528%25EB%2593%25B1%25EC%259E%25A5%25EC%259D%25B8%25EB%25AC%25BC%2529&psig=AOvVaw3gHx84ELnGHQmf0RqgnL5-&ust=1747466752712000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOjd-Im7p40DFQAAAAAdAAAAABAE",
        "traits": {
            "성격 특징": "이성적이고 실용주의자. 도구 활용 능력 뛰어남.",
            "장점 💡": "책임감, 침착함, 문제 해결 능력",
            "단점 ⚠️": "가끔은 너무 현실적이고 감성 부족",
            "잘 어울리는 친구 👯": "진구, 이슬이"
        }
    },
    "도라미": {
        "desc": "똑 부러지고 계획적인 완벽주의자!",
        "img": "https://i.imgur.com/9qgoEo5.png",
        "traits": {
            "성격 특징": "계획적이며 깔끔함. 실수 싫어하는 완벽주의자",
            "장점 💡": "신중하고 체계적, 효율적",
            "단점 ⚠️": "융통성 부족, 실수에 예민",
            "잘 어울리는 친구 👯": "도라에몽, 이슬이"
        }
    },
    "진구": {
        "desc": "조금 덤벙대지만 따뜻한 감성파!",
        "img": "https://www.google.co.kr/url?sa=i&url=https%3A%2F%2Fko.wikipedia.org%2Fwiki%2F%25EB%258F%2584%25EB%259D%25BC%25EC%2597%2590%25EB%25AA%25BD_%2528%25EB%2593%25B1%25EC%259E%25A5%25EC%259D%25B8%25EB%25AC%25BC%2529&psig=AOvVaw3gHx84ELnGHQmf0RqgnL5-&ust=1747466752712000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOjd-Im7p40DFQAAAAAdAAAAABAE",
        "traits": {
            "성격 특징": "게으르지만 정 많고 감성 풍부",
            "장점 💡": "상상력, 순수함, 유연함",
            "단점 ⚠️": "귀찮음, 실행력 부족, 우유부단",
            "잘 어울리는 친구 👯": "도라에몽, 비실이"
        }
    },
    "이슬이": {
        "desc": "예의 바르고 지적인 완벽소녀!",
        "img": "https://i.imgur.com/L8ZH5hf.png",
        "traits": {
            "성격 특징": "차분하고 공감능력 높음, 모범적",
            "장점 💡": "성실함, 정직함, 배려심",
            "단점 ⚠️": "자기감정 억제, 지나치게 착함",
            "잘 어울리는 친구 👯": "도라에몽, 도라미"
        }
    },
    "퉁퉁이": {
        "desc": "자기주장 강하고 열정적인 리더형!",
        "img": "https://i.imgur.com/zxXMeRM.png",
        "traits": {
            "성격 특징": "리더십 있고 솔직함. 다혈질 성향 있음",
            "장점 💡": "결단력, 추진력, 책임감",
            "단점 ⚠️": "고집 셈, 감정 조절 미숙",
            "잘 어울리는 친구 👯": "비실이, 진구"
        }
    },
    "비실이": {
        "desc": "감수성 풍부한 감정형 친구!",
        "img": "https://i.imgur.com/dp6O2qK.png",
        "traits": {
            "성격 특징": "눈물 많고 감정 표현이 풍부",
            "장점 💡": "예술적 감각, 공감력, 감성적",
            "단점 ⚠️": "불안정, 자기비하, 질투심",
            "잘 어울리는 친구 👯": "퉁퉁이, 진구"
        }
    },
}

# 질문 리스트
questions = [
    {"question": "시험 전날 나는...", "A": ("일단 자고 본다", "진구"), "B": ("계획표 짜고 공부한다", "이슬이")},
    {"question": "친구가 울고 있어!", "A": ("같이 울어준다", "비실이"), "B": ("티슈 주고 달래준다", "도라에몽")},
    {"question": "소풍날 비가 오면 나는...", "A": ("그냥 운명인가보다", "진구"), "B": ("대체 플랜을 실행한다!", "도라미")},
    {"question": "친구랑 싸우면 나는...", "A": ("먼저 사과한다", "비실이"), "B": ("그냥 시간 지나길 기다린다", "퉁퉁이")},
    {"question": "먹고 싶은 간식이 떨어졌다면?", "A": ("포기한다", "진구"), "B": ("직접 만들어 먹는다", "도라미")},
    {"question": "단체활동에서 나는...", "A": ("리더를 맡는다", "퉁퉁이"), "B": ("묵묵히 따라간다", "이슬이")},
    {"question": "시험 시간 5분 전, 나는?", "A": ("멘붕", "진구"), "B": ("마지막까지 훑는다", "도라미")},
]

# 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = 0
if "scores" not in st.session_state:
    st.session_state.scores = {char: 0 for char in characters.keys()}

# 테스트 중
if st.session_state.page < len(questions):
    q = questions[st.session_state.page]
    st.markdown(f"### Q{st.session_state.page+1}. {q['question']}")
    st.progress((st.session_state.page + 1) / len(questions))

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🅐 " + q["A"][0]):
            st.session_state.scores[q["A"][1]] += 1
            st.session_state.page += 1
    with col2:
        if st.button("🅑 " + q["B"][0]):
            st.session_state.scores[q["B"][1]] += 1
            st.session_state.page += 1

# 결과 출력
else:
    result = max(st.session_state.scores, key=st.session_state.scores.get)
    st.header(f"당신은 **{result}** 스타일이에요!")
    st.image(characters[result]["img"], width=200)
    st.markdown(f"👉 {characters[result]['desc']}")
    
    # 표로 특성 출력
    traits_df = pd.DataFrame(characters[result]["traits"].items(), columns=["항목", "내용"])
    st.table(traits_df)

    # 다시하기
    if st.button("🔄 다시 하기"):
        st.session_state.page = 0
        st.session_state.scores = {char: 0 for char in characters.keys()}
