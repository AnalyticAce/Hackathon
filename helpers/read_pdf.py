import streamlit as st
import base64
from PIL import Image
import PyPDF2
import requests

@st.cache
def load_lottie(url): 
    req = requests.get(url)
    if req.status_code != 200:
        None
    return req.json()

@st.cache
def get_file_data(file):
    with open(file, 'rb') as f:
        data = f.read()
    return data

@st.cache
def pdf_to_text(file):
    with open(file, "rb") as pdf:
        reader = PyPDF2.PdfFileReader(pdf, strict=False)
        
        text = []
        
        for page in reader.pages:
            content = page.extract_text()
            text.append(content)
            
        return text                                                                                                                                                  