import streamlit as st

def get_resources(topic=None):
    st.subheader("🔗 Resources")

    links = {
        "ai": ["https://arxiv.org/list/cs.AI/recent", "https://www.ibm.com/cloud/learn/what-is-artificial-intelligence"],
        "education": ["https://www.unesco.org/en/themes/education", "https://www.coursera.org/"],
        "healthcare": ["https://www.cdc.gov/", "https://www.who.int/health-topics/healthcare"],
        "environment": ["https://www.epa.gov/", "https://climate.nasa.gov/"],
        "climate change": [
        "https://www.ipcc.ch/report/ar6/syr/",
        "https://climate.nasa.gov/",
    ],
    "artificial intelligence": [
        "https://www.ibm.com/cloud/learn/what-is-artificial-intelligence",
        "https://arxiv.org/list/cs.AI/recent",
    ],
    "mental health": [
        "https://www.who.int/news-room/fact-sheets/detail/mental-health-strengthening-our-response",
        "https://www.apa.org/topics/mental-health",
    ],
    "agriculture": [
        "https://www.fao.org/agriculture",
        "https://www.usda.gov/topics/agriculture",
    ],
    "sports": [
        "https://www.olympic.org/sports",
        "https://www.ncaa.org/",
        "https://www.espn.com/",
    ],
    "education": [
        "https://www.un.org/en/observances/education-day",
        "https://www.unesco.org/en/themes/education",
        "https://www.coursera.org/degrees/education",
    ],
    "technology": [
        "https://www.technologyreview.com/",
        "https://www.techradar.com/",
    ],
    "healthcare": [
        "https://www.who.int/health-topics/healthcare",
        "https://www.cdc.gov/",
    ],
    "environment": [
        "https://www.epa.gov/",
        "https://www.nationalgeographic.com/environment/",
    ],
    "economy": [
        "https://www.imf.org/",
        "https://www.worldbank.org/",
    ],
    "society": [
        "https://www.un.org/en/sections/issues-depth/social/",
        "https://www.undp.org/",
    ],
    "space": [
        "https://www.nasa.gov/",
        "https://www.esa.int/",
    ],
    "travel": [
        "https://www.unwto.org/",
        "https://www.travelandleisure.com/",
    ],
    "food": [
        "https://www.fao.org/",
        "https://www.who.int/news-room/fact-sheets/detail/food-safety-and-food-security",
        "https://www.foodandagriculture.org/",
    ],
    "art": [
        "https://www.artsy.net/",
        "https://www.moma.org/",
        "https://www.artnet.com/",
    ],
    "biotechnology": [
        "https://www.biotechmag.com/",
        "https://www.genengnews.com/",
        "https://www.biotechnology.org/",
    ],
    "digital privacy": [
        "https://www.eff.org/",
        "https://www.privacyinternational.org/",
        "https://www.privacytools.io/",
    ],
    "space colonization": [
        "https://www.space.com/",
        "https://www.nasa.gov/mission_pages/station/research/experiments/1598.html",
        "https://www.spacex.com/",
    ],
    "neurotechnology": [
        "https://www.neurotechx.com/",
        "https://www.neurotechnology.com/",
        "https://www.brainchip.com/",
    ],
    "renewable energy": [
        "https://www.iea.org/",
        "https://www.renewableenergyworld.com/",
        "https://www.renewableenergyfocus.com/",
    ],
    "smart cities": [
        "https://www.smartcitiesworld.net/",
        "https://www.smartcitiesworld.net/",
        "https://www.smartcitiesworld.net/",
    ],
    "personalized medicine": [
        "https://www.personalizedmedicinecoalition.org/",
        "https://www.personalizedmedicine.com/",
        "https://www.personalizedmedicine.com/",
    ],
    "virtual reality": [
        "https://www.virtualrealitytimes.com/",
        "https://www.virtualrealitytimes.com/",
        "https://www.virtualrealitytimes.com/",
    ],
    "sustainable technology": [
        "https://www.sustainabletechnology.net/",
        "https://www.sustainabletechnology.net/",
        "https://www.sustainabletechnology.net/",
    ],
    "ai ethics": [
        "https://www.aeai.org/",
        "https://www.aeai.org/",
        "https://www.aeai.org/",
    ],
    "mHealth": [
        "https://www.mhealthintelligence.com/",
        "https://www.mhealthintelligence.com/",
        "https://www.mhealthintelligence.com/",
    ],
    "telemedicine": [
        "https://www.telemedicine.org/",
        "https://www.telemedicine.org/",
        "https://www.telemedicine.org/",
    ],
    "default": [
        "https://scholar.google.com/",
        "https://www.researchgate.net/",
        "https://www.sciencedirect.com/",
        "https://www.springer.com/",
    ]
}

    if not topic:
        st.write("""
        Here are some general resources for research:
        "Sports", 
        "Art", 
        "Technology", 
        "Society", 
        "Climate Change", 
        "Artificial Intelligence", 
        "Mental Health",
        "Education", 
        "Healthcare",
        "Environment",
        "Economy",
        "Space", 
        "Travel", 
        "Food",
        "Other")
        """)
        topic = st.text_input("Enter the topic you want resources for:").strip()
        if not topic:
            st.info("Please enter a topic to get resources.")
            return

    topic_key = topic.lower()
    topic_links = links.get(topic_key, links["default"])

    st.markdown(f"### Resources for **{topic.title()}**")
    for url in topic_links:
        st.markdown(f"- [{url}]({url})")
