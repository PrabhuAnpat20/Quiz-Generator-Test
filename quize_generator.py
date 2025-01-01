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

# Define the prompt template with conditional logic for MCQs
quiz_prompt = PromptTemplate(
    input_variables=['topic', 'type', 'num', 'subject'],
    template="""Give me {num} {type} questions on {topic} from the subject {subject}.
                If the question type is "Multiple Choice", include the question, answer, and topic in the following JSON structure:
                [
                    {{
                        "question": "Question text",
                        "answer": "Answer text",
                        "topic": "Topic text"
                    }},
                    ...
                ]
                If the question type is not "Multiple Choice", only include the question and answer in the following JSON structure:
                [
                    {{
                        "question": "Question text",
                        "answer": "Answer text"
                    }},
                    ...
                ]
                Give only the questions and answers in JSON format."""
)

# Use LLMChain with a new approach using `RunnableSequence`
chain = quiz_prompt | llm

# Function to generate quiz
def generate_quiz(topic, q_type, num, subject):
        # Pass the correct inputs to the chain
        result = chain.invoke({
            'topic': topic,
            'type': q_type,
            'num': num,
            'subject': subject
        })
        
        # Print the raw result to inspect it
        print("Raw result:", result)
        content=result.content
        cleaned_result=content.strip()
        result_json=json.loads(cleaned_result);  # Inspect the raw result to ensure it’s in JSON format
        return result_json

    #     # Try to parse the result into a JSON object
    #     result_json = json.loads(result.strip())  # Strip any extra whitespace
    #     print("Parsed JSON:", result_json)
    #     return result_json

    # except ValueError as e:
    #     print(f"Error: {e}")
    #     return None

    # except json.decoder.JSONDecodeError as e:
    #     print(f"Error decoding JSON: {e}")
    #     return None

# Generate quiz
generate_quiz("Algebra", "Multiple Choice", 5, "Quadratic Equations")

