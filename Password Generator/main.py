import streamlit as st
import random
import string


st.title("🔑Simple Password Generator🔐")


length = st.number_input("Enter password length:", min_value=4, max_value=50, step=1)


if st.button("Generate Password"):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    st.success(f"Your generated password is: {password}")
