import streamlit as st

def manager():
    if 'youtube_link' not in st.session_state:
        st.session_state['youtube_link'] = []

    with st.expander("Youtube"):
        user_input = st.text_input("Enter Your Youtube videos link")
        add_button = st.button("Add", key='add_button')
        if add_button:
            if len(user_input) > 0:
                st.session_state['youtube_link'] += [user_input]
            else:
                st.warning("Enter Your Youtube videos link")

        for i, item in enumerate(st.session_state['youtube_link']):
            col1, col2 = st.columns([4, 1])
            col1.write(item)
            if col2.button("Delete", key=f'delete_{i}'):
                st.session_state['youtube_link'].remove(item)

    return st.session_state['youtube_link']

if __name__ == '__main__':
    user_list = manager()
    print(user_list)
