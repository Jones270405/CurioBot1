import streamlit as st

def collect_user_profile():
    name = st.text_input("Your Name")
    role = st.selectbox("Your Role", ["Student", "Faculty", "Researcher", "Other"])
    mood = st.selectbox("Your Mood", ["Happy", "Sad", "Angry", "Neutral", "Excited"])
    interests = st.selectbox("Your Interests", ["Sports", "Art", "Technology", "Society", "Climate Change", "Artificial Intelligence", 
        "Mental Health","Education", "Healthcare", "Environment","Economy","Space", "Travel", "Food","Other"])
    return name, role, mood, interests

