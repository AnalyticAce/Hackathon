import streamlit as st
import requests
import configparser

def read_secret_from_config(file_path, section, key):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config.get(section, key)

def init_connection():
    pass

@st.cache_data(show_spinner=False)
def store_data():
    pass

@st.cache_resource(show_spinner=False)
def store_model():
    pass

@st.cache_resource(show_spinner=False)
def load_model(url):
    pass

@st.cache_resource(show_spinner=False)
def run_model(model):
    pass

@st.cache
def get_discussion():
    pass