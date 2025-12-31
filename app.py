import streamlit as st
import pandas as pd
from model import predict_style

st.set_page_config(
    page_title="AI Learning Style Analyzer",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎓 Student Profile")
name = st.sidebar.text_input("Student Name")
age = st.sidebar.number_input("Age", min_value=10, max_value=60, value=18)
course = st.sidebar.text_input("Course / Department")

st.sidebar.markdown("---")
st.sidebar.info("AI-Based Learning Style System\n\nDeveloped for Academic Use")

# ---------------- MAIN TITLE ----------------
st.markdown("""
<h1 style='text-align: center;'>🧠 AI-Based Learning Style Identification System</h1>
<p style='text-align: center; font-size:18px;'>Personalized Learning through Artificial Intelligence</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- INPUT SECTION ----------------
st.subheader("📊 Learning Preference Assessment")

col1, col2 = st.columns(2)

with col1:
    visual = st.slider("📊 Visual Learning", 1, 10, 5)
    auditory = st.slider("🎧 Auditory Learning", 1, 10, 5)

with col2:
    readwrite = st.slider("📖 Reading/Writing", 1, 10, 5)
    kinesthetic = st.slider("🧪 Kinesthetic Learning", 1, 10, 5)

# ---------------- BUTTON ----------------
if st.button("🔍 Analyze Learning Style"):
    style = predict_style([visual, auditory, readwrite, kinesthetic])

    st.success(f"✅ Predicted Learning Style: **{style}**")

    # ---------------- VISUALIZATION ----------------
    st.subheader("📈 Learning Preference Distribution")

    data = {
        "Visual": visual,
        "Auditory": auditory,
        "Read/Write": readwrite,
        "Kinesthetic": kinesthetic
    }

    df = pd.DataFrame(list(data.items()), columns=["Type", "Score"])

    st.bar_chart(df.set_index("Type"))

    # ---------------- RECOMMENDATION ----------------
    st.subheader("🎯 Personalized Learning Recommendation")

    if style == "Visual":
        st.info("✔ Use diagrams, infographics, mind maps, and videos.")
    elif style == "Auditory":
        st.info("✔ Prefer lectures, podcasts, group discussions.")
    elif style == "ReadWrite":
        st.info("✔ Learn through textbooks, note-making, summaries.")
    else:
        st.info("✔ Learn via hands-on practice, experiments, and simulations.")

    st.markdown("---")
    st.caption("📌 AI Model: Random Forest Classifier | Dataset: Simulated Academic Dataset")


