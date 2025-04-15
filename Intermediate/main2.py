import streamlit as st
import random
bouncing_header = """
<style>
.stApp {
    background-color: #ffe4f0; /* Light funky pink */
}

@keyframes bounce {
  0% { transform: translateY(0); }
  25% { transform: translateY(-10px); }
  50% { transform: translateY(0); }
  75% { transform: translateY(-5px); }
  100% { transform: translateY(0); }
}

.animated-title {
  display: inline-block;
  font-size: 48px;
  font-weight: bold;
  color: #22c55e; /* emerald green */
  animation: bounce 1s infinite;
  text-align: center;
  font-family:  "Comic Sans MS", sans-serif
}
</style>

<div style="text-align: center;">
  <span class="animated-title">🎮 High-Low Game</span>
</div>
"""

st.markdown(bouncing_header, unsafe_allow_html=True)
st.markdown('<h3 style="text-align: center;">Will you go High or Low?</h3>', unsafe_allow_html=True)
# Initialize session state
if 'round' not in st.session_state:
    st.session_state.round = 1
    st.session_state.score = 0
    st.session_state.your_number = random.randint(1, 100)
    st.session_state.computer_number = random.randint(1, 100)

NUM_ROUNDS = 5

# Display round info
st.markdown(f"### Round {st.session_state.round} of {NUM_ROUNDS}")
st.write(f"Your number is: **{st.session_state.your_number}**")

# 3D-style button layout using columns
col1, col2 = st.columns(2)
with col1:
    if st.button("🔼 Higher"):
        if st.session_state.your_number > st.session_state.computer_number:
            st.success("✅ Correct! Your number was higher.")
            st.session_state.score += 1
        else:
            st.error("❌ Nope! Your number wasn't higher.")
        st.session_state.round += 1

with col2:
    if st.button("🔽 Lower"):
        if st.session_state.your_number < st.session_state.computer_number:
            st.success("✅ Correct! Your number was lower.")
            st.session_state.score += 1
        else:
            st.error("❌ Nope! Your number wasn't lower.")
        st.session_state.round += 1

# End of game logic
if st.session_state.round > NUM_ROUNDS:
    st.markdown("## 🏁 Game Over!")
    st.write(f"🎯 Final Score: **{st.session_state.score} / {NUM_ROUNDS}**")
    if st.button("🔁 Play Again"):
        st.session_state.round = 1
        st.session_state.score = 0
# Prepare next round
if st.session_state.round <= NUM_ROUNDS:
    st.session_state.your_number = random.randint(1, 100)
    st.session_state.computer_number = random.randint(1, 100)
