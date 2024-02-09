import streamlit as st
import base64
from PIL import Image
import PyPDF2
import requests

@st.cache_data(show_spinner=False)
def load_lottie(url): 
    req = requests.get(url)
    if req.status_code != 200:
        None
    return req.json()

@st.cache_data(show_spinner=False)
def get_file_data(file):
    with open(file, 'rb') as f:
        data = f.read()
    return data

@st.cache_data(show_spinner=False)
def pdf_to_text(file):

    reader = PyPDF2.PdfFileReader(file, strict=False)
    
    text = []
    
    for page in reader.pages:
        content = page.extract_text()
        text.append(content)
        
    return text                                                                                                                                              