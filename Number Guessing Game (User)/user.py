import streamlit as st
import random

def main():
    st.title("🎯🎮 Number Guessing Game!")
    st.write("I'm thinking of a number between 1 and 100. You have only **5 attempts**. Good luck!")

    st.markdown(
        """
        <style>
        .stApp {
            background-color: #e8f5e9; /* Lightest green shade */
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px 15px;
            font-size: 16px;
            margin-top: 10px;
            border: 2px solid #1b1b1b;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if 'random_number' not in st.session_state:
        st.session_state.random_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False

    if not st.session_state.game_over:
        guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
        st.info(f"Attempts left: {5 - st.session_state.attempts}")

        if st.button("Submit Guess"):
            st.session_state.attempts += 1

            if guess < st.session_state.random_number:
                st.warning("Too low! Guess a higher number.")
            elif guess > st.session_state.random_number:
                st.warning("Too high! Guess a lower number.")
            else:
                st.success(f"🎉 Correct! The number was {st.session_state.random_number}. You got it in {st.session_state.attempts} attempts!")
                st.balloons()
                st.session_state.game_over = True

            if st.session_state.attempts >= 5 and not st.session_state.game_over:
                st.error(f"Game Over! You've used all 5 chances. The correct number was {st.session_state.random_number}.")
                st.session_state.game_over = True

    if st.session_state.game_over:
        if st.button("Play Again"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]

if __name__ == "__main__":
    main()
