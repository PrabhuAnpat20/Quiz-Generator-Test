import streamlit as st
from quize_generator import generate_quiz

# Set the title of the app
st.title("Quiz Generator")

# Main topics and their respective sub-topics
topics = {
    "Algebra": ["Linear Equations", "Quadratic Equations", "Polynomials"],
    "Geometry": ["Triangles", "Circles", "Coordinate Geometry"],
    "Trigonometry": ["Basic Ratios", "Trigonometric Identities", "Applications"],
    "Calculus": ["Differentiation", "Integration", "Limits"],
    "Statistics": ["Descriptive Statistics", "Inferential Statistics", "Probability Distributions"],
    "Probability": ["Basic Concepts", "Conditional Probability", "Bayesian Probability"]
}

# Topic selection
selected_topic = st.sidebar.selectbox("Choose a topic", list(topics.keys()))

# Sub-topic selection
if selected_topic:
    sub_topics = topics[selected_topic]
    selected_sub_topic = st.sidebar.selectbox(f"Choose a sub-topic under {selected_topic}", sub_topics)

# Number of questions input
num_questions = st.sidebar.number_input("Number of questions", min_value=1, max_value=20, value=5)

# Generate Quiz button
if st.sidebar.button("Generate Quiz"):
    # Pass both topic and sub-topic to the quiz generator
    quiz = generate_quiz(selected_topic, selected_sub_topic, num_questions)
    st.write(f"### Quiz on {selected_topic} - {selected_sub_topic}")
    st.write(quiz)
