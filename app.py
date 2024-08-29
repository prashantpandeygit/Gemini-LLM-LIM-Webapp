from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://static.vecteezy.com/system/resources/previews/014/729/918/original/abstract-dark-purple-3d-background-with-purple-and-white-lines-paper-cut-style-textured-usable-for-decorative-web-layout-poster-banner-corporate-brochure-and-seminar-template-design-vector.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0, 0, 0, 0);
}
[data-testid="stSidebar"] {
    background: rgba(0, 0, 0, 0);
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_pro_response(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question, stream=True)
    return response

def get_gemini_flash_response(image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(image)
    return response.text


st.header("Gemini LLM & LIM Application")
input_text = st.text_input("Enter your question:")
submit_text = st.button("Generate Response", key="text_submit")

if submit_text:
    if input_text:
        response = get_gemini_pro_response(input_text)
        for chunk in response:
            st.write(chunk.text)
    else:
        st.error("Please enter a question before generating a response.")

st.markdown("---")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

submit_image = st.button("Generate Response", key="image_submit")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if submit_image:
        response = get_gemini_flash_response(image)
        st.write(response)
elif submit_image:
    st.warning("Please upload an image before generating a response.")
