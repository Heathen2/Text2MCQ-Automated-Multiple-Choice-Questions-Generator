import streamlit as st
from lang_xtract import get_quiz


gpt_key = st.text_input("openai key")
if gpt_key:
    file_to_process = st.file_uploader("Upload the file",type=["pdf"])
    if file_to_process:
        process_btn = st.button("Extract")
        if process_btn:
            with st.spinner("Extracting"):
                with open("input_to_process.pdf",'wb') as file:
                    file.write(file_to_process.getvalue())
                response = get_quiz(gpt_key, "input_to_process.pdf")
            st.success("Extracted and saved") 
            st.write(response)