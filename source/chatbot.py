import streamlit as st
import pandas as pd
from time import *
import time
import numpy as np

#https://docs.streamlit.io/library/api-reference/write-magic/st.write_stream

st.set_page_config(
    page_title="MySupport",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

ANSWER_ = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""

if 'page' not in st.session_state:
    st.session_state.page = 'home'

if st.session_state.page == 'home':
    if 'first_time' not in st.session_state:
        st.session_state.first_time = False

    st.title("Welcome to :blue[MySup]:red[port]", anchor=False)
    st.write("""
    Are you looking to provide personalized support to your customers? Do you want to leverage the power of AI to answer customer queries? If yes, then **MySupport** is the perfect tool for you!

    **How does it work?** 🤔
    1. Enter the link to your Trained Model.
    2. Press the start button and follow the instructions.

    ⚠️ **Important:** Your Trained Model Link must be valid to move to the next step.

    Once you've input your model link, voilà! You're ready to start the discussion with your custom assistant. Press the ***:red[Start Discussion]*** Button and follow the instructions to engage with your AI-powered chatbot. Let's revolutionize customer support together!
    """)

    with st.expander("💡 Video Tutorial"):
        with st.spinner("Loading video.."):
            st.video("https://youtu.be/22Ee9ayzfTU?si=o1WSepWVuqsV3Jt6", format="video/mp4", start_time=0)

    with st.form("user_input"):
        MODEL_LINK = st.text_input("Enter your Trained Model Link:", placeholder="http://")

        submitted = st.form_submit_button("Start Discussion", type="primary")
        
        if submitted:
            with st.status("***:blue[Creating ChatBot 🤖...]***"):
                st.write("***:red[Searching for Model 🕵️‍♂️...]***")
                sleep(2)
                st.write("***:blue[Found Model 🔗.]***")
                sleep(1)
                st.write("***:red[Initializing Bot 🔃...]***")
                sleep(1)

        if not MODEL_LINK:
            st.info("Please fill out the Trained Model Link to proceed. If you don't have one, you can obtain it here.")
            st.stop()

        st.session_state.MODEL_LINK = MODEL_LINK

        st.session_state.page = 'ChatBot'
        st.rerun()

elif st.session_state.page == 'ChatBot':
    MODEL_LINK = st.session_state.get('MODEL_LINK')
    
    if not MODEL_LINK:
        st.warning("Model not found. Please enter the key on the home page.")
        st.stop()
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
        
    if prompt := st.chat_input("How can we help you ?"):

        with st.chat_message("user"):
            st.markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            def stream_data():
                for word in ANSWER_.split():
                    yield word + " "
                    time.sleep(0.02)

            paragraph = ""
            for data in stream_data():
                paragraph += data + " "
            st.write(paragraph)

        st.session_state.messages.append({"role": "assistant", "content": paragraph})
