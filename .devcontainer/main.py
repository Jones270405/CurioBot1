import streamlit as st
import user_profile, topic_explorer
from drafting_assistant import draft_research_paper
from resource_finder import get_resources


st.set_page_config(page_title="CurioBot", layout="centered")
st.title("🎓 CurioBot: Your Research Thinking Assistant")

with st.sidebar:
    st.header("👤 User Profile")
    name, role, mood, interests = user_profile.collect_user_profile()

if name and interests:
    wants_interest = st.radio(
        "Would you like to research one of your interests?",
        ["Yes", "No"]
    )

    if wants_interest == "Yes":
        selected_interest = interests

        st.success(f"Hi {name}! Ready to explore **{selected_interest}** today?")
        topic_explorer.show_topic_info(selected_interest)

        # Optional: Direct resource search for selected interest
        if st.button("📚 Get Resources for this topic"):
            get_resources(selected_interest)

    else:
        st.info(f"Hi {name}! You can choose to explore another topic, draft a research paper, or get resources.")
        choice = st.radio("What would you like to do?", [
            "🔍 Explore Another Topic", "📝 Draft Research Paper", "📚 Get Resources"
        ])

        if choice == "🔍 Explore Another Topic":
            all_topics = ["Sports", "Art", "Technology", "Society", "Climate Change", "Artificial Intelligence", 
        "Mental Health","Education", "Healthcare", "Environment","Economy","Space", "Travel", "Food","Other"]
            other_topics = [t for t in all_topics if t not in interests]
            selected_topic = st.selectbox("Select a topic to explore:", other_topics)
            topic_explorer.show_topic_info(selected_topic)
        elif choice == "📝 Draft Research Paper":
            draft_research_paper()
        elif choice == "📚 Get Resources":
            get_resources()  # Will prompt for topic if not provided

else:
    st.warning("Please fill in your profile to begin.")
