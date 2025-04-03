# import streamlit as st
# 
# st.title("BMI Calculator")
# weight = st.number_input("Enter your weight (kg):", min_value=1.0 , step=1.0)
# height = st.number_input("Enter your height (m):" , min_value=0.1 , step= 0.01)
# 
# def calculate_bmi(weight , height):
#     if height > 0:
#         return weight / (height ** 2)
#     else:
#         return None
# 
# if st.button("Calculate BMI"):
#     bmi = calculate_bmi(weight , height)
#     if bmi:
#         st.success(f"Your BMI is: {bmi:.2f}")
#         if bmi < 18.5:
#             st.warning("You are underweight.")
#         elif 18.5 <= bmi < 35.9:
#             st.success("Your Weight Is Normal")
#         elif 25 <= bmi < 40.9:
#             st.warning("You are overweight.")
#         else:
#             st.error("You are obese.")
#     else:
#         st.error("Please enter a valid height.")
# 
# 
# 
#
