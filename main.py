import streamlit as st
import pandas as pd

st.set_page_config(page_title="도라에몽 캐릭터 심리 테스트", page_icon="🤖")

# 캐릭터 데이터
characters = {
    "도라에몽": {
        "desc": "문제를 해결해주는 든든한 해결사! 차분하고 배려심이 깊어요.",
        "img": "https://i.imgur.com/H5IwBqX.png",
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
        "desc": "순수하고 정 많은 감성파!",
        "img": "https://i.imgur.com/vgUcoTr.png",
        "traits": {
            "성격 특징": "게으르지만 상상력 풍부, 감정적임",
            "장점 💡": "공감 능력, 창의성",
            "단점 ⚠️": "실행력 부족, 우유부단",
            "잘 어울리는 친구 👯": "도라에몽, 비실이"
        }
    },
    "이슬이": {
        "desc": "침착하고 공감 잘하는 지성파!",
        "img": "https://i.imgur.com/L8ZH5hf.png",
        "traits": {
            "성격 특징": "지적이고 예의 바르며 감정 조절에 능함",
            "장점 💡": "이해심, 배려심, 학업성실",
            "단점 ⚠️": "감정 숨기기, 지나치게 착함",
            "잘 어울리는 친구 👯": "도라미, 도라에몽"
        }
    },
    "퉁퉁이": {
        "desc": "강한 리더십과 열정을 가진 추진형!",
        "img": "https://i.imgur.com/zxXMeRM.png",
        "traits": {
            "성격 특징": "직설적이며 자기주장 강함",
            "장점 💡": "리더십, 추진력",
            "단점 ⚠️": "고집 셈, 감정 조절 부족",
            "잘 어울리는 친구 👯": "비실이, 진구"
        }
    },
    "비실이": {
        "desc": "섬세하고 감수성 풍부한 감성캐!",
        "img": "https://i.imgur.com/QyaH0Sn.png",
        "traits": {
            "성격 특징": "소심하지만 감정이 풍부하고 예술적",
            "장점 💡": "감수성, 공감력",
            "단점 ⚠️": "소심함, 자존감 낮음",
            "잘 어울리는 친구 👯": "진구, 이슬이"
        }
    }
}

# 질문 목록
questions = [
    {"question": "시험 전날 나는...", "A": ("일단 자고 본다", "진구"), "B": ("계획표 짜고 공부한다", "이슬이")},
    {"question": "친구가 울고 있어!", "A": ("같이 울어준다", "비실이"), "B": ("티슈 주고 달래준다", "도라에몽")},
    {"question": "소풍날 비가 오면 나는...", "A": ("운명인가보다", "진구"), "B": ("대체 플랜 실행!", "도라미")},
    {"question": "친구랑 싸우면 나는...", "A": ("먼저 사과함", "비실이"), "B": ("시간이 해결해주겠지", "퉁퉁이")},
    {"question": "간식이 떨어졌다면?", "A": ("포기한다", "진구"), "B": ("직접 만들어 먹는다", "도라미")},
    {"question": "단체활동에서 나는...", "A": ("리더를 맡는다", "퉁퉁이"), "B": ("조용히 따라간다", "이슬이")},
    {"question": "시험 시간 5분 전, 나는?", "A": ("멘붕!", "진구"), "B": ("마지막까지 훑는다", "도라미")}
]

# 초기 상태 설정
if "page" not in st.session_state:
    st.session_state.page = 0
if "scores" not in st.session_state:
    st.session_state.scores = {name: 0 for name in characters.keys()}

st.title("🤖 도라에몽 캐릭터 심리 테스트")
st.write("당신과 닮은 도라에몽 캐릭터는 누구일까요?")

# 질문 표시
if st.session_state.page < len(questions):
    q = questions[st.session_state.page]
    st.progress((st.session_state.page + 1) / len(questions))
    st.subheader(f"Q{st.session_state.page + 1}. {q['question']}")
    col1, col2 = st.columns(2)
    if col1.button(q['A'][0]):
        st.session_state.scores[q['A'][1]] += 1
        st.session_state.page += 1
    if col2.button(q['B'][0]):
        st.session_state.scores[q['B'][1]] += 1
        st.session_state.page += 1

# 결과 표시
else:
    st.subheader("🎉 결과 분석")

    # 최고 점수 캐릭터 찾기
    result = max(st.session_state.scores, key=st.session_state.scores.get)
    char_data = characters[result]

    st.image(char_data["img"], width=250)
    st.markdown(f"### 당신은 **{result}** 타입!")
    st.write(char_data["desc"])

    # 표로 특징 출력
    df = pd.DataFrame(char_data["traits"].items(), columns=["항목", "내용"])
    st.table(df)

    st.markdown("---")
    if st.button("🔁 다시하기"):
        st.session_state.page = 0
        st.session_state.scores = {name: 0 for name in characters.keys()}



