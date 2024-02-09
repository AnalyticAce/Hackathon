# import streamlit as st

# def upload_pdf_files():
#     if 'uploaded_files' not in st.session_state:
#         st.session_state['uploaded_files'] = []

#     with st.expander("PDF Upload"):
#         uploaded_file = st.file_uploader("Upload a PDF file", type=['pdf'])
#         if uploaded_file is not None:
#             st.session_state['uploaded_files'] += [uploaded_file]
#             st.success("File uploaded successfully!")

#         for i, item in enumerate(st.session_state['uploaded_files']):
#             col1, col2 = st.columns([4, 1])
#             col1.write(item.name)
#             if col2.button("Delete", key=f'delete_{i}'):
#                 st.session_state['uploaded_files'].remove(item)
#                 st.success(f"File deleted successfully!")

#     return st.session_state['uploaded_files']

# if __name__ == '__main__':
#     user_list = upload_pdf_files()
#     print(user_list)

import sys

print(sys.path)  # Check current Python path

sys.path.append('/home/dosseh/Data/Project/Hackathon/Assitant/helpers/read_file')  # Add 'helpers' directory to Python path

import helpers  # Now Python should be able to import 'helpers'
