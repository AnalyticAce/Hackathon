import streamlit as st
import requests
import configparser

def read_secret_from_config(file_path, section, key):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config.get(section, key)

@st.cache_resource
def init_connection():
    pass

@st.cache
def store_data():
    pass

@st.cache_resource
def store_model():
    pass

@st.cache_resource
def load_model(url):
    pass

@st.cache_resource
def run_model(url):
    pass

@st.cache
def get_discussion():
    pass