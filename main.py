import streamlit as st
from quize_generator import generate_quiz
# Set the title of the app
st.title("Math Quiz Generator")

topics = ["Algebra", "Geometry", "Trigonometry", "Calculus", "Statistics", "Probability"]
question_types = ["Multiple Choice", "Fill in the blanks", "True/False"]


selected_topic = st.sidebar.selectbox("Choose a topic", topics)
selected_type = st.sidebar.selectbox("Choose question type", question_types)
num_questions = st.sidebar.number_input("Number of questions", min_value=1, max_value=20, value=5)

if st.sidebar.button("Generate Quiz"):
    quiz = generate_quiz(selected_topic, selected_type,num_questions)
    st.write(f"### Quiz on {selected_topic} - {selected_type}")
    st.write(quiz)