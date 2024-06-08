from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from typing import List, Optional
from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_community.document_loaders import PyMuPDFLoader
import pandas as pd
from datetime import datetime
import os

if not os.path.exists('temp'):
        os.makedirs('temp')
quiz_list = []

class Question(BaseModel):
    """A quiz question along with multiple choice options and the correct answer."""
    question: str = Field(default=None, description="The quiz question.")
    option_a: str = Field(default=None, description="Option a for the question.")
    option_b: str = Field(default=None, description="Option b for the question.")
    option_c: str = Field(default=None, description="Option c for the question.")
    option_d: str = Field(default=None, description="Option d for the question.")
    correct_answer_option: str = Field(default=None, description="The correct answer option for the question.")
    answer_explanation: str = Field(default=None, description="The very brief explanation for the correct answer.")

class Data(BaseModel):
    """Quiz questions."""
    Questions: List[Question]


def extract_quiz(api_key,file_content):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an expert teacher who is preparing structured MCQ questions for an exam. "
                "Analyze the texbook passage to understand and then create a structured question, four options, correct answer option and answer explanation from the passage."
                "The passage and generated questions might have many errors which should be corrected, So you should always examine and fix the errors in all the questions, options, correct answer options and answer explanations"
            ),

            ("human", "{text}"),
        ]
    )

    llm = ChatOpenAI(model="gpt-3.5-turbo",temperature=0,max_tokens=None,timeout=None,max_retries=2, api_key =api_key)
    questions = []
    runnable = prompt | llm.with_structured_output(schema=Data)
    
    for page in file_content:
        response = runnable.invoke({"text": page.page_content})
        questions.extend(response.Questions)
        quiz_list.extend(response.Questions)

    # Convert questions to dictionary for easier handling
    data = {
        "question": [q.question for q in questions],
        "option1": [q.option_a for q in questions],
        "option2": [q.option_b for q in questions],
        "option3": [q.option_c for q in questions],
        "option4": [q.option_d for q in questions],
        "correct_answer": [q.correct_answer_option for q in questions],
        "answer_explanation": [q.answer_explanation for q in questions]
    }

    # Convert dictionary to DataFrame
    df = pd.DataFrame(data)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"temp/Questions_{timestamp}.xlsx"
    # Write DataFrame to Excel file
    df.to_excel(file_name, index=False)




def get_quiz(api_key, doc_name):
    loader = PyMuPDFLoader(doc_name)
    text_splitter =  CharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=500,
        chunk_overlap=20,
        # length_function=len,
        # is_separator_regex=False,
    )
    file_content = loader.load_and_split(text_splitter=text_splitter)
    file_content_length = len(file_content)
    for i in range(0, file_content_length, 20):
        if i + 20 > file_content_length:
            extract_quiz(api_key,file_content[i:file_content_length])
        else:
            extract_quiz(api_key,file_content[i:i+20])        

    data = {
            "question": [q.question for q in quiz_list],
            "option1": [q.option_a for q in quiz_list],
            "option2": [q.option_b for q in quiz_list],
            "option3": [q.option_c for q in quiz_list],
            "option4": [q.option_d for q in quiz_list],
            "correct_answer": [q.correct_answer_option for q in quiz_list],
            "answer_explanation": [q.answer_explanation for q in quiz_list]
        }

    # Convert dictionary to DataFrame
    df = pd.DataFrame(data)
    # Write DataFrame to Excel file
    df.to_excel("Final_Quiz.xlsx", index=False)
    return df