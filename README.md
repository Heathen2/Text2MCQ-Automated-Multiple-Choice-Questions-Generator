**MCQ Generator**

All credit goes to Langchain & Streamlit for this project.

Demo - https://quiz-from-text-sn4bynrj7s9thvymsiqccq.streamlit.app/

**Overview**

MCQ Generator is a Python application powered by GPT that allows users to upload documents and generate multiple-choice questions (MCQs) in a structured format. Built with LangChain and Streamlit, this application aims to facilitate the creation of quizzes, assessments, or study materials by automating the process of question generation.

**Features**

Document Upload: Users can upload text documents in various formats (e.g., PDF, DOCX, TXT) containing the content from which MCQs need to be generated.

Question Generation: The application utilizes LangChain, a natural language processing library, to analyze the uploaded documents and generate relevant multiple-choice questions.

MCQ Sheet Creation: Generated MCQs are presented in a standardized format suitable for printing or digital sharing, facilitating easy integration into educational materials or assessments.

Streamlit Interface: The user-friendly Streamlit interface ensures seamless interaction, allowing users to upload documents and obtain MCQ outputs effortlessly.


**Installation**

To run the LangChain MCQ Generator locally, follow these steps:

Clone the repository:

bash

    git clone https://github.com/Heathen2/quiz-from-text.git

Navigate to the project directory:

bash

    cd quiz-from-text

Install the required dependencies:

    pip install -r requirements.txt

Run the application:

    streamlit run streamlit_app.py

**Usage**

Launch the application by running streamlit run streamlit_app.py.
Upload a document containing the content for which MCQs need to be generated.
Click on the "Extract" button to initiate the question generation process.
Once the MCQs are generated, they will be displayed on the interface.
Optionally, you can Download the generated MCQs as a formatted sheet for further use.
