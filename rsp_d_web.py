import streamlit as st
from PIL import Image
import random

def 가위바위보(user_choice):
    choices = ["가위", "바위", "보"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "비겼습니다."
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        result = "이겼습니다. 집에 갑니다!"
    else:
        result = "졌습니다. 카페에 갑니다!"

    return user_choice, computer_choice, result

st.title("가위바위보 게임")

# 이미지 로드
rock_img = Image.open("rock.png")
scissors_img = Image.open("scissors.png")
paper_img = Image.open("paper.png")

# 이미지 버튼
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("바위", key='rock'):
        user_choice = "바위"
        user_choice, computer_choice, result = 가위바위보(user_choice)
        st.write(f"사용자 선택: {user_choice}")
        st.write(f"컴퓨터 선택: {computer_choice}")
        st.write(f"결과: {result}")
    st.image(rock_img, use_column_width=True)

with col2:
    if st.button("가위", key='scissors'):
        user_choice = "가위"
        user_choice, computer_choice, result = 가위바위보(user_choice)
        st.write(f"사용자 선택: {user_choice}")
        st.write(f"컴퓨터 선택: {computer_choice}")
        st.write(f"결과: {result}")
    st.image(scissors_img, use_column_width=True)

with col3:
    if st.button("보", key='paper'):
        user_choice = "보"
        user_choice, computer_choice, result = 가위바위보(user_choice)
        st.write(f"사용자 선택: {user_choice}")
        st.write(f"컴퓨터 선택: {computer_choice}")
        st.write(f"결과: {result}")
    st.image(paper_img, use_column_width=True)
