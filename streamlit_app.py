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
                st.session_state["response"] = response
            st.success("Extracted and saved")
            with open("Final_Quiz.xlsx", "rb") as file:
                btn = st.download_button(
                label="Download",
                data=file,
                file_name="Final_Quiz.xlsx",
                )
            st.write(st.session_state["response"])
