import streamlit as st
import time

st.title("⏳ Countdown Timer")
page_style = """
<style>
.stApp {
    background-color: #fffacd;  
}
button {
    background-color: darkorange !important; 
    color: white !important;
    font-weight: bold;
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)
seconds = st.number_input("Enter time in seconds:", min_value=1, step=1)


if st.button("Start Timer"):
    st.write("Timer started!")

    
    countdown_area = st.empty()

   
    for i in range(int(seconds), 0, -1):
        countdown_area.write(f"{i} seconds left")
        time.sleep(1)

    
    countdown_area.write("⏰ Time's up!")
