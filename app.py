import streamlit as st
import requests
import io
from PIL import Image
# import base64
# from dotenv import load_dotenv
# import os

# Load environment variables from the .env file
# load_dotenv()
# bearer_token = os.environ.get('BEARER_TOKEN')
# print("bearer", bearer_token)

# token = st.secrets["BEARER_TOKEN"]

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": f"Bearer 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"}

st.title("Text to Image")

# Create a two-column layout
col1, col2 = st.columns(2)

# Text input on the left
with col1:
    txt = st.text_area('Enter text below to generate')

# Button on the left
with col1:
    if 'button' not in st.session_state:
        st.session_state.button = False

    def query():
        response = requests.post(API_URL, headers=headers, json={
            "inputs": txt,  # Use the user-provided text here
        })
        return response.content

    def click_button():
        st.session_state.button = not st.session_state.button

    st.button('Generate', on_click=click_button)

# Placeholder for the image on the right
with col2:

	image_bytes = query()
	img = Image.open(io.BytesIO(image_bytes))
	image_base64 = base64.b64encode(image_bytes).decode()

        # Apply HTML and CSS for rounded corners
	img_html = f'<img src="data:image/png;base64,{image_base64}" style="border-radius: 10px; height:450px">'
	st.markdown(img_html, unsafe_allow_html=True)



