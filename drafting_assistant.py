import streamlit as st

def draft_research_paper():
    st.title("📄 Research Paper Drafting Assistant")
    
    st.subheader("📋 Research Paper Format Reference")
    with st.expander("Click to view the recommended format"):
        st.markdown("""
            1. **TITLE PAGE**  
            - Paper title (centered, bold)  
            - Author name(s)  
            - Institution/affiliation  
            - Date  

            2. **ABSTRACT (150-250 words)**  
            - Brief summary of the entire paper  

            3. **INTRODUCTION**  
            - Background information  
            - Research objectives/questions  

            4. **LITERATURE REVIEW**  
            - Existing research, gaps, your position  

            5. **METHODOLOGY**  
            - Research design, data collection, limitations  

            6. **RESULTS/FINDINGS**  
            - Charts, data presentation  

            7. **DISCUSSION**  
            - Interpretation, comparison with prior studies  

            8. **CONCLUSION**  
            - Key takeaways and future work  

            9. **REFERENCES**  
            - APA or MLA citation style  

            10. **APPENDICES**  
            - Additional content, graphs, etc.
        """)

    st.subheader("📝 Enter Your Research Paper Content")

    topic = st.text_input("Research Topic")
    intro = st.text_area("✍️ Introduction")
    abstract = st.text_area("📝 Abstract (150–250 words)")
    litreview = st.text_area("📚 Literature Review")
    method = st.text_area("🔬 Methodology")
    results = st.text_area("📊 Expected Results")
    discussion = st.text_area("💬 Discussion")
    conclusion = st.text_area("🔚 Conclusion")
    references = st.text_area("📚 References (APA Format)")
    appendices = st.text_area("📋 Appendices (optional)")

    # Only one Generate Draft button, with a unique key
    if st.button("📌 Generate Draft", key="generate_draft_btn"):
        st.session_state['draft_generated'] = True

        st.success(f"Here's your draft on: **{topic}**")

        st.markdown("### 📄 Draft Overview")
        st.write(f"**Introduction**: {intro}")
        st.write(f"**Abstract**: {abstract}")
        st.write(f"**Literature Review**: {litreview}")
        st.write(f"**Methodology**: {method}")
        st.write(f"**Expected Results**: {results}")
        st.write(f"**Discussion**: {discussion}")
        st.write(f"**Conclusion**: {conclusion}")
        st.write(f"**References**: {references}")
        st.write(f"**Appendices**: {appendices}")

        # Save to file
        with open("Research_Draft.txt", "w", encoding="utf-8") as f:
            f.write(f"Topic: {topic}\n")
            f.write("Introduction: " + intro + "\n")
            f.write("Abstract: " + abstract + "\n")
            f.write("Literature Review: " + litreview + "\n")
            f.write("Methodology: " + method + "\n")
            f.write("Expected Results: " + results + "\n")
            f.write("Discussion: " + discussion + "\n")
            f.write("Conclusion: " + conclusion + "\n")
            f.write("References: " + references + "\n")
            f.write("Appendices: " + appendices + "\n")

        st.success("✅ Research draft saved to **Research_Draft.txt**")

    # Show citation generator only after draft is generated
    if st.session_state.get('draft_generated', False):
        st.subheader("📖 Generate APA Citation")

        author = st.text_input("👤 Author's full name", key="author")
        title = st.text_input("📘 Title of article or book", key="title")
        year = st.text_input("📅 Year of publication", key="year")
        source = st.text_input("🔗 Source or publisher", key="source")

        if st.button("📚 Generate Citation", key="generate_citation_btn"):
            citation = f"{author} ({year}). *{title}*. {source}."
            st.session_state['citation'] = citation

        if 'citation' in st.session_state:
            st.code(st.session_state['citation'], language='markdown')
            st.info("Copy and use this in your references section.")

    # Feedback and Word Count
    import re

    def count_words(text):
        if not text:
            return 0
        # This regex counts words including apostrophes and hyphens
        words = re.findall(r"\b[\w'-]+\b", text)
        return len(words)
    
    sections = [intro, abstract, litreview, method, results, discussion, conclusion]
    total_words = sum(count_words(s) for s in sections)
    st.markdown(f"**📏 Total Word Count**: `{total_words}`")


    if total_words < 100:
        st.warning("Your paper is quite short. Expand each section.")
        score = "Needs Significant Improvement"
    elif total_words < 200:
        st.info("Good start! Add more details.")
        score = "Developing"
    elif total_words < 300:
        st.success("Nice work! Paper is developing well.")
        score = "Well Developed"
    else:
        st.success("🌟 Excellent! Your paper is comprehensive.")
        score = "Excellent"

    st.markdown(f"**🏆 Overall Assessment**: `{score}`")
