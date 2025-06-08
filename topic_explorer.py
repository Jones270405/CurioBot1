import streamlit as st
import get_resources

# Dictionary: topic -> description
topic_list = {
    "Climate Change": "Environmental science, sustainability, global warming",
    "Artificial Intelligence": "Machine learning, robotics, AI ethics",
    "Mental Health": "Psychology, wellness, therapy methods",
    "Agriculture": "Farming techniques, food security",
    "Sports": "Athletic performance, psychology, fitness",
    "Education": "EdTech, pedagogy, teacher training",
    "Technology": "Innovation, cybersecurity, automation",
    "Healthcare": "Telemedicine, mHealth, diagnostics",
    "Environment": "Pollution, conservation, biodiversity",
    "Economy": "Global trade, finance, development",
    "Society": "Social justice, culture, community dev",
    "Space": "Exploration, astrophysics, colonization",
    "Travel": "Tourism, cultural exchange",
    "Food": "Nutrition, security, food tech"
}

def show_topic_info(topic):
    topic_key = topic.lower()
    st.markdown(f"## 🎯 {topic.title()}")
    summaries = {
    "climate change":
    "Climate change refers to long-term shifts in temperatures and weather patterns, primarily caused by human activities such as burning fossil fuels.",
    "artificial intelligence":
    "AI refers to the simulation of human intelligence by machines, enabling them to learn, reason, and make decisions.",
    "mental health":
    "Mental health refers to cognitive, behavioral, and emotional well-being. It is essential for daily living and overall quality of life.",
    "agriculture":
    "Agriculture is the practice of cultivating plants and livestock for food, fiber, and other products.",
    "sports":
    "Sports involve physical activity and competition, often organized and governed by rules and regulations.",
    "education":
    "Education is the process of facilitating learning, or the acquisition of knowledge, skills, values, morals, beliefs, and habits.",
    "technology":
    "Technology encompasses the tools, machines, techniques, and systems that make human life easier and more efficient.",
    "healthcare":
    "Healthcare refers to the maintenance or improvement of health via the prevention, diagnosis, treatment, recovery, or cure of disease, illness, injury, and other physical and mental impairments in people.",
    "environment":
    "The environment encompasses all living and non-living things occurring naturally on Earth or some region thereof.",
    "economy":
    "An economy is a region where goods and services are made and traded.",
    "society":
    "Society is a group of people who live in the same geographical area and share common values, norms, and customs.",
    "space":
    "Space is the boundless three-dimensional extent in which objects and events have relative position and direction.",
    "travel":
    "Travel is the movement of people between distant geographical locations.",
    "food":
    "Food is any substance consumed to provide nutritional support for an organism.",
    "art":
    "Art is a diverse range of human activities in creating visual, auditory, or performing artifacts (artworks), expressing the author's imaginative, conceptual ideas, or technical skill, intended to be appreciated for their beauty or emotional power.",
    "ai ethics":
    "AI ethics is the study of the ethical implications of artificial intelligence.",
    "biotechnology":
    "Biotechnology is the use of biological organisms, systems, or processes to create or modify products for specific use.",
    "digital privacy":
    "Digital privacy refers to the ability of individuals to control the collection, use, and dissemination of their personal data.",
    "space colonization":
    "Space colonization involves the establishment of human settlements in outer space, such as on the Moon or Mars.",
    "neurotechnology":
    "Neurotechnology is the use of technology to study, understand, and manipulate the brain and nervous system.",
    "renewable energy":
    "Renewable energy is energy that is collected from renewable resources, which are naturally replenished on a human timescale.",
    "smart cities":
    "Smart cities use digital technology to improve the quality of life for their citizens.",
    "personalized medicine":
    "Personalized medicine is a medical approach that uses an individual's genetic profile to guide treatment decisions.",
    "virtual reality":
    "Virtual reality is a simulated experience that can be similar to or completely different from the real world.",
    "sustainable technology":
    "Sustainable technology is technology that is designed to minimize environmental impact and promote sustainability.",
    "mHealth":
    "mHealth is the use of mobile devices and wireless technology to improve health outcomes.",
    "telemedicine":
    "Telemedicine is the use of telecommunications and information technology to provide clinical health care from a distance.",
    "healthcare innovation":
    "Healthcare innovation is the introduction of new ideas, processes, or products into healthcare.",
    "default": "This topic is not covered in the current database."
}

    related_topics = {
        "Artificial Intelligence": ["Ethical AI", "AI in education", "AI in healthcare"],
        "Climate Change": ["Carbon neutrality", "Green energy", "Climate policy"],
        "Mental Health": ["Digital therapy", "Social media & anxiety", "Campus wellness"],
        "Education": ["Online learning", "Inclusive pedagogy", "Gamification"],
        "climate change":
        ["carbon neutrality", "renewable energy", "global warming effects"],
        "artificial intelligence":
        ["machine learning", "ethics in AI", "AI in education"],
        "mental health":
        ["student stress", "therapy methods", "social media and anxiety"],
        "agriculture":
        ["organic farming", "agri-fintech", "drought-resistant crops"],
        "sports":
        ["youth sports", "gender equality in sports", "sports and mental health"],
        "education": ["online learning", "special education", "teacher training"],
        "technology":
        ["cybersecurity", "5G technology", "blockchain", "sustainable technology"],
        "healthcare": ["telemedicine", "mHealth", "healthcare innovation"],
        "environment":
        ["plastic pollution", "biodiversity loss", "climate resilience"],
        "economy": ["financial literacy", "economic inequality", "global trade"],
        "society":
        ["social justice", "community development", "cultural diversity"],
        "space": ["space exploration", "space tourism", "space debris"],
        "travel": ["sustainable tourism", "travel safety", "cultural tourism"],
        "food": ["food security", "food waste reduction", "nutritional health"],
        "art": ["art therapy", "art education", "art and mental health"],
        "ai ethics": ["ethics in AI", "AI and society", "AI regulation"],
        "sustainable technology":
        ["green innovations", "environmental technology", "sustainable practices"],
        "biotechnology":
        ["genetic engineering", "CRISPR", "medical breakthroughs"],
        "digital privacy":
        ["data protection", "cybersecurity", "online privacy rights"],
        "space colonization":
        ["Mars missions", "space habitats", "interplanetary travel"],
        "neurotechnology": [
            "brain-computer interfaces", "cognitive enhancement", "neural implants"
        ],
        "renewable energy": [
            "solar energy", "wind energy", "clean energy solutions"
        ],
        "smart cities": ["IoT", "urban planning", "technology-integrated cities"],
        "personalized medicine": [
            "genetic testing", "precision treatments", "health tech"
        ],
        "virtual reality": [
            "VR applications", "education", "therapy", "entertainment"
        ],
        "default":
        ["interdisciplinary studies", "emerging trends", "practical applications"]
    }

    st.markdown("### 📝 Topic Summary")
    st.write(summaries.get(topic_key, summaries["default"]))

    st.markdown("### 🔍 Related Research Areas")
    for rel in related_topics.get(topic_key, related_topics["default"]):
        st.markdown(f"• {rel}")
  
    st.markdown("### 🚀 Research & Innovation Culture")
    st.markdown("• [Research Methodology](https://www.researchgate.net/publication/research-methodology)")
    st.markdown("• [Innovation Thinking (TED)](https://www.ted.com/topics/innovation)")
    st.markdown("• [Scientific Method (Nature)](https://www.nature.com/articles/research-methods)")
    st.markdown("• [Data Analysis Courses](https://www.coursera.org/courses?query=data%20analysis)")
    st.markdown("• [Research Ethics](https://www.researchethics.org/)")
    st.markdown("• [Research Integrity](https://www.researchintegrity.org/)")
    st.markdown("### 📚 Further Reading")
    st.markdown("• [ResearchGate](https://www.researchgate.net/)")
    
    
