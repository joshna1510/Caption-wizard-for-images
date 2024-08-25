import io
import os
import streamlit as st
from PIL import Image
from model import get_caption_model, generate_caption
from translate import Translator

# Set page title and icon
st.set_page_config(
    page_title="Image Captioning App",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f7f7f7;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .stApp {
            max-width: 800px;
            margin: auto;
            padding: 2em;
        }
        hr {
            margin: 2em 0;
            border: none;
            border-top: 1px solid #ccc;
        }
        footer {
            text-align: center;
            color: #888;
            margin-top: 2em;
        }
    </style>
    """,
    unsafe_allow_html=True
)

caption_model = get_caption_model()

# Header
st.title('Image Captioner')
st.write("Generate captions for images and get translations in English, Telugu and Hindi.")

def predict():
    pred_caption = generate_caption("tmp.jpg", caption_model)
    st.markdown("#### Predicted Captions:")
    st.markdown(f"<p style='font-size: 24px; font-weight: bold; color: #4a4a4a;'>{pred_caption}</p>", unsafe_allow_html=True)

# Upload image section
img_upload = st.file_uploader(label='Choose an image', type=['jpg', 'png', 'jpeg'])

# Predict and display results
if img_upload:
    img = Image.open(io.BytesIO(img_upload.read()))
    img = img.convert('RGB')
    img.save('tmp.jpg')

    # Image preview
    st.image(img, caption='Uploaded Image', use_column_width=True)

    # Predicted captions and translations
    with st.spinner("Generating captions..."):
        predict()

    # Remove temporary image file
    os.remove('tmp.jpg')
    
st.markdown('<hr>', unsafe_allow_html=True)

# Footer
st.markdown('<footer>Developed with CNN and Transformers</footer>', unsafe_allow_html=True)
