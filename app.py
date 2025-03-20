import streamlit as st
import random

def main():
    st.title("🤖 Computer-Based Number Guessing Game")
    st.write("Think of a number between **1 and 100**, and let me guess!")

    
    st.markdown("""
        <style>
        .stApp {
            background-color: #FFF4E6;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: 2px solid #1b1b1b;
            border-radius: 10px;
            padding: 10px 15px;
            font-size: 16px;
            margin-top: 10px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        </style>
        """, unsafe_allow_html=True)

    # Initialize session variables
    if 'low' not in st.session_state:
        st.session_state.low = 1
    if 'high' not in st.session_state:
        st.session_state.high = 100
    if 'guess' not in st.session_state:
        st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False

    if not st.session_state.game_over:
        st.subheader(f"My Guess: {st.session_state.guess}")
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Too High"):
                st.session_state.high = st.session_state.guess - 1
        with col2:
            if st.button("Too Low"):
                st.session_state.low = st.session_state.guess + 1
        with col3:
            if st.button("Correct!"):
                st.success(f"🎉 Yay! I guessed your number: {st.session_state.guess}")
                st.balloons()
                st.session_state.game_over = True

        # Update guess after feedback
        if not st.session_state.game_over:
            if st.session_state.low <= st.session_state.high:
                st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
            else:
                st.error("Hmm... It seems there's an inconsistency! Please restart.")

    else:
        if st.button("Play Again"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]

if __name__ == "__main__":
    main()
