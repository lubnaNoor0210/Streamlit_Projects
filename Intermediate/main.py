import streamlit as st

st.set_page_config(
    page_title="Planet Weight Calculator",
    page_icon="🌍",
    layout="centered")

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://t3.ftcdn.net/jpg/08/41/16/64/360_F_841166454_o5WVAfwoeDq5AGbqKYxDrkyn0WiGCmPz.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
 
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.markdown("""
    <style>
    h1 {
        color: white; 
    }
    p {
        color: white; 
    }
    body {
        color: white; 
    }
    .stButton > button {
        background-color:  #000000;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color: white;'>🪐 Planet Weight Calculator</h1>", unsafe_allow_html=True)


st.markdown("Ever wondered how much you'd weigh on another planet? Let's find out!")

MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
EARTH_GRAVITY = 1.0
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

gravity_constants = {
    "Mercury": MERCURY_GRAVITY,
    "Venus": VENUS_GRAVITY,
    "Earth": EARTH_GRAVITY,
    "Mars": MARS_GRAVITY,
    "Jupiter": JUPITER_GRAVITY,
    "Saturn": SATURN_GRAVITY,
    "Uranus": URANUS_GRAVITY,
    "Neptune": NEPTUNE_GRAVITY
}

earth_weight = st.number_input("Enter your weight on Earth (kg):", min_value=0.0, format="%.2f")

planet = st.selectbox("Select a planet:", list(gravity_constants.keys()))

if st.button("Calculate"):
    if earth_weight > 0:
        gravity_constant = gravity_constants[planet]
        planetary_weight = earth_weight * gravity_constant
        rounded_weight = round(planetary_weight, 2)
        st.success(f"🌎 Your weight on {planet} would be **{rounded_weight} kg**.")
    else:
        st.error("Please enter a valid weight on Earth.")