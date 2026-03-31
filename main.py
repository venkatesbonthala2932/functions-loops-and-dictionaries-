import streamlit as st 
st.write("Hello World 1234  5678") 
pressed=st.button("Press me")
if pressed: 
    st.write("You pressed the button!")
else:    st.write("You haven't pressed the button yet.")
pressed2=st.button("Press me too")
if pressed2:    st.write("You pressed the second button!")
else:    st.write("You haven't pressed the second button yet.") 