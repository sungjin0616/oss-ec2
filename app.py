import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="OSS 실습 3 EC2 배포",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 OSS 실습 3 - EC2 Streamlit 배포")
st.subheader("간단한 메모 앱")

st.write(
    """
    2025404041 강성진
    """
)

st.divider()

st.header("간단한 입력 테스트")

name = st.text_input("이름을 입력하세요", placeholder="예: 강성진")

message = st.text_area(
    "간단히 할말을 입력하세요",
    placeholder="예: 안녕하세요 강성진입니다."
)

satisfaction = st.slider(
    "앱 실행 만족도",
    min_value=1,
    max_value=5,
    value=5
)

st.divider()

if st.button("결과 확인하기"):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if name.strip() == "":
        st.warning("이름을 입력해주세요.")
        print(f"[EC2 LOG] {current_time} - 이름이 입력되지 않았습니다.")
    elif message.strip() == "":
        st.warning("메시지를 입력해주세요.")
        print(f"[EC2 LOG] {current_time} - 메시지가 입력되지 않았습니다. name={name}")
    else:
        st.success("입력 결과가 정상적으로 처리되었습니다.")

        st.write("### 입력 결과")
        st.write(f"**이름:** {name}")
        st.write(f"**메시지:** {message}")
        st.write(f"**만족도:** {satisfaction}점")
        st.write(f"**처리 시간:** {current_time}")

        print(
            f"[EC2 LOG] {current_time} - "
            f"name={name}, message={message}, satisfaction={satisfaction}"
        )

st.divider()
