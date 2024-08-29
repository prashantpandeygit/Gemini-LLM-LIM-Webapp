from dotenv import load_dotenv
# to load environment variables
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro") 
def get_gemini_response(question):
    response=model.generate_content(question,stream=True)
    return response


st.header("Gemini LLM Application")


input=st.text_input("Input: ",key="input")
submit=st.button("Generate Response")

if submit and input:
    response=get_gemini_response(input)
    st.subheader("Response: ")
    for chunk in response:
        st.write(chunk.text)

