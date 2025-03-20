import streamlit as st
st.markdown("""
    <style>
   
    .stApp {
        background-color: #F3E5F5;
    }

    
    .custom-title { 
        font-family: Arial, sans-serif !important;
        font-size: 40px;
        font-weight: bold;
        color: pink;
        text-align: center;
    }      
            
    div[data-testid="stTextInput"] {
        width: 80% !important;  
        margin: auto;  
    }


     div[data-testid="stTextInput"] input {
        font-size: 18px !important;  
        padding: 12px !important;  
        border: 2px solid #6A1B9A !important;  
        border-radius: 8px !important;  
        background-color: #FDFEFE !important;  
        color: #333333 !important;  
        width: 100% !important;  
        box-shadow: none !important;  
    }

    </style>
    """, unsafe_allow_html=True)

def main():
    
    st.markdown("<h1 class='custom-title'>🎭 Fun Mad Libs Game!</h1>", unsafe_allow_html=True)
    
    st.write("Fill in the blanks below and create your own magical story!")

   
    name = st.text_input("Enter a name:")
    magical_item = st.text_input("Enter a magical item:")
    verb = st.text_input("Enter a verb:")
    place = st.text_input("Enter a place:")
    creature = st.text_input("Enter an animal:")
    emotion = st.text_input("Enter an emotion:")

  
    if st.button("Generate Story✨🎆"):
        if name and magical_item and verb and place and creature and emotion:
            story = f"""
            In the mystical land of {place}, a young adventurer named {name} set out on a journey.
            One day, {name} discovered a hidden cave where a {creature} guarded an ancient {magical_item}.
            Determined, {name} decided to {verb} towards the treasure.
            Suddenly, the {creature} roared with {emotion}, shaking the entire cave!
            But instead of fighting, {name} cleverly used the power of kindness.
            The {creature} smiled, handed over the {magical_item}, and vanished into the mist.
            With a heart full of excitement, {name} returned home, knowing that true magic lies in bravery and friendship.
            """
            st.success("Here’s your Mad Libs Story!")
            st.write(story)
        else:
            st.warning("Please fill in all fields before generating the story.")
if __name__ == "__main__":
    main()
