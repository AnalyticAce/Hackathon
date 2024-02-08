#!/bin/bash

python3 -m pip install --upgrade pip
pip install -r  requirements.txt
streamlit run source/chatbot.py
