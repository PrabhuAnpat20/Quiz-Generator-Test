import streamlit as st
from quize_generator import generate_quiz
import json

# Set the title of the app
st.title("Quiz Generator")

subjects = ["Algebra", "Geometry", "Trigonometry", "Calculus", "Statistics", "Probability"]
question_types = ["Multiple Choice", "True/False"]

selected_subject = st.sidebar.selectbox("Choose a subject", subjects)
selected_topic = st.sidebar.text_input("Enter a topic")
selected_type = st.sidebar.selectbox("Choose question type", question_types)
num_questions = st.sidebar.number_input("Number of questions", min_value=1, max_value=20, value=5)

if st.sidebar.button("Generate Quiz"):
    if selected_topic.strip() == "":
        st.error("Please enter a topic.")
    else:
        quiz = generate_quiz(selected_topic, selected_type, num_questions, selected_subject)

        # Debugging step: print the type and value of the quiz data
        # st.write(f"Type of quiz: {type(quiz)}")  # Show the type of quiz
        # st.write(f"Quiz content: {quiz}")  # Show the actual quiz content

        # Check if the quiz was generated successfully
        if quiz:
            st.write(f"### Quiz on {selected_topic} - {selected_type}")

            try:
                # If quiz is a JSON string, parse it
                if isinstance(quiz, str):
                    quiz_json = json.loads(quiz)  # Try to convert the string to a dictionary
                    st.json(quiz_json)  # Display the quiz as a formatted JSON in Streamlit
                elif isinstance(quiz, (dict, list)):
                    st.json(quiz)  # If it's already a valid dictionary/list, display it

            except json.JSONDecodeError as e:
                st.error(f"Error decoding quiz data: {e}")
        
        else:
            st.error("Failed to generate the quiz. Please try again.")
