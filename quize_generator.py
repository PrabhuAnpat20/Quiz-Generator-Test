from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
import json
from langchain.chains import LLMChain

# Load .env variables
load_dotenv()

# Access the API key
groq_api_key = os.getenv("GROQ_API_KEY")

# Ensure the API key is set properly
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is missing in .env file")

# Initialize the LLM with Groq
llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    groq_api_key=groq_api_key
)


quiz_prompt = PromptTemplate(
    input_variables=['topic','subTopic','num'],
    template="""Give me {num} multiple choice questions on {topic} {subTopic}. 
    Provide only the questions, options, correct answer, and a difficulty rating in JSON format. 
    Example:
    {{
        "question": "What is the sum of interior angles in a triangle?",
        "options": ["180", "270", "360", "450"],
        "answer": 1,
        "difficulty": 0.3
        "topic":{topic}
        "subTopic":{subTopic}
    }}
    """
)
chain=LLMChain(llm=llm,prompt=quiz_prompt)

def generate_quiz(topic,sub_topic,num):
    result = chain.run({'topic': topic,'subTopic':sub_topic,'num':num})
    return result