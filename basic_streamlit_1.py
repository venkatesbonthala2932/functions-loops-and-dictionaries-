import streamlit as st
from message_tools import welcome

st.title("Basic Streamlit App")
name =st.text_input("enter your name : ")
if st.button("show welcome message"):
    if name.strip() != "":
        st.success(welcome(name))
    else:
        st.error("Please enter your name to see the welcome message.")