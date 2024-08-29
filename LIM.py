from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(image)
    return response.text

st.title("Gemini LIM Application")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


submit = st.button("Generate Response")
image = Image.open(uploaded_file)
st.image(image, caption="Uploaded Image.", use_column_width=True)


if submit:
    response = get_gemini_response(image)
    st.write(response)
