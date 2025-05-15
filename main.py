import streamlit as st

st.title("🎉 트랄라렐로트랄라라 MBTI 테스트 🎉")
st.write("10개의 질문에 답하고, 나의 트랄라라 성격을 알아보자!")

questions = [
    ("파티에서 나는…", "사람들과 어울리는 게 좋아", "조용히 구석에서 쉬는 게 좋아", "EI"),
    ("계획 세우는 걸 좋아해?", "물론이지!", "즉흥이 더 재밌지~", "JP"),
    ("친구가 고민을 털어놨어. 나는…", "논리적으로 해결책 제시", "공감하고 위로", "TF"),
    ("여행 가기 전 나는…", "계획 철저", "가서 정함", "JP"),
    ("새로운 아이디어는…", "좋아! 창의적이야", "현실적인 게 좋아", "SN"),
    ("사람 많은 곳은…", "에너지 넘쳐", "좀 피곤해", "EI"),
    ("영화 볼 때 나는…", "상징을 찾아냄", "스토리에 집중", "SN"),
    ("중요한 결정은…", "논리를 따름", "느낌을 따름", "TF"),
    ("친구들과 놀 때 나는…", "내가 리드함", "따라감", "EI"),
    ("생일 선물 고를 때…", "실용적인 거", "감성적인 거", "TF"),
]

answers = []

for i, (q, a1, a2, typ) in enumerate(questions):
    choice = st.radio(f"{i+1}. {q}", (a1, a2), key=i)
    answers.append((choice, typ, a1))

if st.button("결과 보기"):
    result = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

    for answer, typ, a1 in answers:
        if typ == "EI":
            result["E" if answer == a1 else "I"] += 1
        elif typ == "SN":
            result["S" if answer == a1 else "N"] += 1
        elif typ == "TF":
            result["T" if answer == a1 else "F"] += 1
        elif typ == "JP":
            result["J" if answer == a1 else "P"] += 1

    mbti = "".join([
        "E" if result["E"] >= result["I"] else "I",
        "S" if result["S"] >= result["N"] else "N",
        "T" if result["T"] >= result["F"] else "F",
        "J" if result["J"] >= result["P"] else "P"
    ])

    st.subheader(f"🎊 당신의 트랄라라 MBTI는: {mbti} 🎊")
    st.write(f"설명: (여기에 {mbti} 유형의 재미있는 캐릭터 설명 넣기)")

