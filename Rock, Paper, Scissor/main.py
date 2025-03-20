import streamlit as st
import random


st.set_page_config(page_title="Rock Paper Scissors", layout="centered")


page_bg = """
<style>
.stApp {
    background-color: #f5f5dc; 
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("🎮 Rock, Paper, Scissors Game!")


choices = ["Rock", "Paper", "Scissors"]


user_choice = st.selectbox("Choose your move:", choices)


if st.button("Play"):
    computer_choice = random.choice(choices)
    st.write(f"🧑 You chose: **{user_choice}**")
    st.write(f"💻 Computer chose: **{computer_choice}**")
    st.balloons()

    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You win!"
    else:
        result = "😢 You lose!"


    st.subheader(result)


st.write("---")
st.write("Made for fun using Streamlit")

