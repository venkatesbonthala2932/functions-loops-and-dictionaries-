import streamlit as st 

st.title("**user information**")
with st.form(key="my_form"):
    name=st.text_input("Enter your name : ")
    number=st.number_input("Enter your number : ")
    email=st.text_input("Enter your email : ")
    st.form_submit_button("Submit")
print(name,"\t",number,"\t",email)
