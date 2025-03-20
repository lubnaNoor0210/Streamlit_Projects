import streamlit as st
import random

st.set_page_config(page_title="Hangman Game", layout="centered")

page_bg = """
<style>
.stApp {
    background-color: #ffe6f0;  /* Lightest pink shade */
}
<style>
"""

st.markdown(page_bg, unsafe_allow_html = True)

words = ["grapes", "orange", "banana", "peach", "apple", "melon"]

if'word' not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.attempts=5
    st.session_state.guessed_letters=[]
    st.session_state.result=""

word=st.session_state.word
attempts=st.session_state.attempts
guessed_letters= st.session_state.guessed_letters

display_word="".join([letter if letter in guessed_letters else"-"for letter in word])
st.header("🎩Let's Play Hangman!")
st.markdown("""
<div style="border: 2px solid black; padding: 10px; border-radius: 8px; background-color: #f9f9f9; text-align: center; margin-bottom: 20px;">
<strong>Hint:</strong> Fruits
</div>
""", unsafe_allow_html=True)


st.write(f"Word:{display_word}")
st.write(f"Attempts left:{attempts}")

guess=st.text_input("Enter a letter:").lower()

if st.button("Guess"):
    if guess and guess.isalpha() and len(guess) == 1:
        if guess in guessed_letters:
            st.warning("You already guessed that letter!")
        elif guess in word:
            st.session_state.guessed_letters.append(guess)
            st.session_state.attempts -= 1
            st.error(f"Oops! '{guess}' is not in the word.")
        else:
            st.warning("Please enter a single letter.")
if all(letter in guessed_letters for letter in word):
    st.balloons()
    st.success(f"🥳You Guessed the word '{word}'! You Win!")
    st.session_state.result="win"

if attempts <=0 and st.session_state.result != "win":
    st.error(f"Game Over! The word was '{word}'.")
    st.session_state.result="lose"

if st.session_state.result:
    if st.button("Play Again"):
        st.session_state.word= random.choice(words)
        st.session_state.attempts=5
        st.session_state.guessed_letters = []
        st.session_state.result= ""

st.write("--")
st.write("Made with 💌 for learning")                    
