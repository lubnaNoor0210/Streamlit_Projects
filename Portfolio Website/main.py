import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFCCCC;  
    }
    .stMarkdown {
        color: darkblue;
    }
     .link-box {
        background-color: #FFB6C1;  /* Light pink color */
        padding: 10px;
        margin: 10px;
        border-radius: 5px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .link-box a {
        color: black;
        font-weight: bold;
        text-decoration: none;
    }

    .link-box a:hover {
        text-decoration: underline;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Welcome to My Website🖥️")
st.subheader("Welcome to my portfolio! I'm Lubna, a beginner web developer passionate about building dynamic applications. I'm still learning, but I'm excited to share my journey and projects with you."
)

st.markdown(
    '<h2 style="font-weight: bold; font-size: 28px;">Here are some of the projects I\'ve created with Streamlit.⬇️</h2>',
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="link-box">
        <a href="https://appprojects-x3evu5wpymmo46yhc8ydve.streamlit.app/" target="_blank">Password Generator🔑</a>
    </div>
     <div class="link-box">
        <a href="https://password-strength-checker-wvfebnuvujzdh3qz4ajdjj.streamlit.app/" target="_blank">Password Strenth Checker🔐</a>
    </div>  
     <div class="link-box">
        <a href="https://appprojects-dsunqgx2vpqor8cv3hwvmq.streamlit.app/" target="_blank">HangMan Game🎩</a>
    </div>
    <div class="link-box">
        <a href="https://appprojects-gg6tqrt7frpq5qnywwzce3.streamlit.app/" target="_blank">Rock Paper Scissor🪨🗞️✂️</a>
    </div>  
   <div class="link-box">
        <a href="https://unit-converter-shcjadjeash3ni9bphajak.streamlit.app/" target="_blank">Unit Converter⌛</a>
    </div>
    """,
    unsafe_allow_html=True
)
