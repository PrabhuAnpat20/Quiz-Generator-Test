from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
# Load .env variables
load_dotenv()

# Access the API key
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    groq_api_key=groq_api_key
)


quiz_prompt=PromptTemplate(
    input_variables=['topic','type','num'],
    template="Give me {num} {type} questions  on {topic}.give only the questions and answers no other info"
    )

chain=LLMChain(llm=llm,prompt=quiz_prompt)

def generate_quiz(topic, q_type,num):
    result = chain.run({'topic': topic, 'type': q_type,'num':num})
    print(result)
    return result